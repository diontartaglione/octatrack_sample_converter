#!/bin/bash
# Installation script for octatrack-converter

set -e

echo "Installing Octatrack Converter..."

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Build the Docker image
echo "Building Docker image..."
docker build -t octatrack-converter "$SCRIPT_DIR"

# Make the wrapper script executable
echo "Setting up wrapper script..."
chmod +x "$SCRIPT_DIR/octatrack-convert"

# Create symlink in /usr/local/bin
echo "Creating symlink in /usr/local/bin..."
if [ -L "/usr/local/bin/octatrack-convert" ]; then
    echo "Removing existing symlink..."
    sudo rm /usr/local/bin/octatrack-convert
fi

sudo ln -s "$SCRIPT_DIR/octatrack-convert" /usr/local/bin/octatrack-convert

echo ""
echo "✓ Installation complete!"
echo ""
echo "You can now use 'octatrack-convert' from any directory:"
echo "  octatrack-convert                          # 16-bit conversion"
echo "  octatrack-convert --bit-depth 24           # 24-bit conversion"
echo "  octatrack-convert --bit-depth 24 --rename  # 24-bit with renamed files"
echo ""
