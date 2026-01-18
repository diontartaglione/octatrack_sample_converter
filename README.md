# Octatrack Sample Converter

A Docker-based audio file converter that processes audio samples to make them compatible with the Octatrack sampler. The converter uses ffmpeg to convert audio files to 44.1kHz sample rate and 16/24-bit depth.

## Features

- Converts multiple audio formats: WAV, AIFF, AIF, FLAC, MP3, OGG
- Maintains directory structure in the output
- Batch processes all audio files in subdirectories
- Outputs to a dedicated folder: `octrack_converted_16bit` or `octrack_converted_24bit`

## Requirements

- Docker

## Installation

### Quick Install (Recommended)

Run the install script from the project directory:

```bash
chmod +x install.sh
./install.sh
```

This will:
1. Build the Docker image
2. Make the wrapper script executable
3. Create a symlink in `/usr/local/bin`
4. Note: You will prompted for your password to create the symlink.

After installation, you can use `octatrack-convert` from any directory!

### Manual Installation

If you prefer to install manually:

```bash
# Build the Docker image
docker build -t octatrack-converter .

# Make wrapper script executable
chmod +x octatrack-convert

# Create symlink (requires sudo)
sudo ln -s "$(pwd)/octatrack-convert" /usr/local/bin/octatrack-convert
```

### Uninstall

To uninstall:

```bash
./uninstall.sh
```

## Usage

### Using the installed command (after running install.sh)

1. Navigate to the directory containing your audio samples.
2. Run the converter with desired options.

```bash
# 16-bit conversion
octatrack-convert

# 24-bit conversion
octatrack-convert --bit-depth 24

# With renamed files
octatrack-convert --bit-depth 24 --rename
```

## Command Line Options

- `--bit-depth`: Choose bit depth for conversion (default: 16)
  - `16`: 16-bit output
  - `24`: 24-bit output
- `--rename`: Append sample rate and bit depth to output filenames
  - Example: `kick.wav` becomes `kick_44100_16.wav`
  - Useful for identifying converted files at a glance

## Output

Converted files will be saved in a new directory:
- `octrack_converted_16bit` for 16-bit conversions
- `octrack_converted_24bit` for 24-bit conversions

Output format:
- Sample rate: 44.1kHz
- Bit depth: 16-bit or 24-bit (as specified)
- Same directory structure as the input

## Example

```
input/
├── drums/
│   ├── kick.wav
│   └── snare.aiff
└── synths/
    └── bass.flac

After conversion:

input/
├── octrack_converted_16bit/
│   ├── drums/
│   │   ├── kick.wav
│   │   └── snare.aiff
│   └── synths/
│       └── bass.flac
```

