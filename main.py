import argparse
import os
import subprocess


def main():
    parser = argparse.ArgumentParser(
        description="Convert audio files for Octatrack compatibility"
    )
    parser.add_argument(
        "--bit-depth",
        type=int,
        choices=[16, 24],
        default=16,
        help="Bit depth for conversion (16 or 24, default: 16)",
    )
    parser.add_argument(
        "--rename",
        action="store_true",
        help="Append sample rate and bit depth to output filenames (e.g., filename_44100_16.wav)",
    )

    args = parser.parse_args()

    sample_rate = 44100
    bit_depth = args.bit_depth

    # Get the current working directory
    cwd = os.getcwd()

    # create a directory to copy files into.
    dir_suffix = "_renamed" if args.rename else ""
    copy_dir = os.path.join(cwd, f"octrack_converted_{bit_depth}bit{dir_suffix}")
    os.makedirs(copy_dir, exist_ok=True)

    # Walk the directory tree from the current directory
    for dirpath, _, filenames in os.walk(cwd):
        # Skip any output directories (current and previous runs)
        if "octrack_converted_" in dirpath:
            continue

        for filename in filenames:
            # Only process audio files
            if not filename.lower().endswith(
                (".wav", ".aiff", ".aif", ".flac", ".mp3", ".ogg")
            ):
                continue

            print(f"Processing file: {filename}")

            # build source path
            src_file_path = os.path.join(dirpath, filename)

            # Get relative path from cwd and build destination path
            relative_path = os.path.relpath(src_file_path, cwd)

            # Add sample rate and bit depth to filename if --rename flag is set
            if args.rename:
                base_name, ext = os.path.splitext(relative_path)
                relative_path = f"{base_name}_{bit_depth}bit_{sample_rate}{ext}"

            dest_file_path = os.path.join(copy_dir, relative_path)

            # Create destination directory structure
            os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)

            # use ffmpeg to convert the audio file
            # For 24-bit, use s32 format (24-bit samples in 32-bit container)
            sample_fmt = "s16" if bit_depth == 16 else "s32"

            cmd = [
                "ffmpeg",
                "-i",
                src_file_path,
                "-ar",
                str(sample_rate),
                "-sample_fmt",
                sample_fmt,
                "-acodec",
                "pcm_s24le" if bit_depth == 24 else "pcm_s16le",
                "-y",  # overwrite output files
                dest_file_path,
            ]

            try:
                subprocess.run(cmd, check=True, capture_output=True)
                print(f"    Converted to: {dest_file_path}")
            except subprocess.CalledProcessError as e:
                print(f"    Error converting {filename}: {e.stderr.decode()}")


if __name__ == "__main__":
    main()
