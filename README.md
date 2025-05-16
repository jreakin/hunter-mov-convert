# Hunter MOV Converter

A simple command-line tool to convert MOV files to MP4 format.

## Prerequisites

### Installing Git on Windows

1. Download Git for Windows from the official website:
   - Visit [https://git-scm.com/download/win](https://git-scm.com/download/win)
   - The download should start automatically
   - If not, click the "Click here to download" link

2. Run the installer:
   - Double-click the downloaded file (usually named something like "Git-2.x.x-64-bit.exe")
   - Accept the default options (or customize if you prefer)
   - Click "Next" through the installer
   - Click "Install" to begin installation

3. Verify the installation:
   - Open Command Prompt or PowerShell
   - Type `git --version`
   - You should see the Git version number if installed correctly

### Using Windows PowerShell

To navigate to a folder in Windows PowerShell:

1. Open PowerShell:
   - Press `Windows + X` and select "Windows PowerShell" or "Terminal"
   - Or search for "PowerShell" in the Start menu

2. Navigate to a folder:
   ```powershell
   # List current directory contents
   dir
   
   # Change to a specific folder
   cd C:\path\to\your\folder
   
   # Go up one directory
   cd ..
   
   # Go to your user directory
   cd ~
   
   # Go to a specific drive (e.g., D:)
   D:
   ```

3. Useful commands:
   ```powershell
   # Show current directory
   pwd
   
   # List all files and folders
   dir
   
   # Create a new folder
   mkdir new-folder-name
   
   # Remove a folder
   rm folder-name
   ```

## Installation

### Quick Install (Recommended)

We provide a setup script that will automatically install uv (if needed) and the package:

```bash
# Clone the repository
git clone https://github.com/yourusername/hunter-mov-convert.git
cd hunter-mov-convert

# Run the setup script
./setup.sh
```

### Manual Installation

You can also install this package directly from GitHub using either pip or uv:

Using pip:
```bash
pip install git+https://github.com/yourusername/hunter-mov-convert.git
```

Using uv (faster):
```bash
uv pip install git+https://github.com/yourusername/hunter-mov-convert.git
```

Or if you've cloned the repository:

Using pip:
```bash
cd hunter-mov-convert
pip install .
```

Using uv:
```bash
cd hunter-mov-convert
uv pip install .
```

## Usage

After installation, you can run the program using uv:

```bash
uv run python -m hunter_mov_convert.main /path/to/your/mov/folder
```

The tool will:
1. Create a new `mp4` subfolder in your input folder
2. Convert all MOV files in the input folder to MP4 format
3. Save the converted files in the `mp4` subfolder

## Requirements

- Python 3.8 or higher
- Git (for cloning the repository)
- moviepy
- tqdm
- curl (for automatic uv installation)
