#!/bin/bash

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "uv is not installed. Installing uv..."
    
    # Check if curl is available
    if command -v curl &> /dev/null; then
        curl -LsSf https://astral.sh/uv/install.sh | sh
    else
        echo "Error: curl is not installed. Please install curl first."
        exit 1
    fi
fi

# Install the package using uv
echo "Installing hunter-mov-convert..."
uv pip install .

echo "Installation complete!"
echo ""
echo "You can now run the program using one of these methods:"
echo "1. python -m hunter_mov_convert.main /path/to/your/mov/folder"
echo "2. hunter-converter /path/to/your/mov/folder (if the command is in your PATH)"
echo ""
echo "If the 'hunter-converter' command doesn't work, use the first method." 