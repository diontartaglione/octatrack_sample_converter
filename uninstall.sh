#!/bin/bash
# Uninstallation script for octatrack-converter

set -e

echo "Uninstalling Octatrack Converter..."

# Remove symlink
if [ -L "/usr/local/bin/octatrack-convert" ]; then
    echo "Removing symlink from /usr/local/bin..."
    sudo rm /usr/local/bin/octatrack-convert
    echo "✓ Symlink removed"
else
    echo "No symlink found at /usr/local/bin/octatrack-convert"
fi

# Ask if user wants to remove Docker image
read -p "Do you want to remove the Docker image? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Removing Docker image..."
    docker rmi octatrack-converter 2>/dev/null && echo "✓ Docker image removed" || echo "Docker image not found"
fi

echo ""
echo "✓ Uninstallation complete!"
echo ""
