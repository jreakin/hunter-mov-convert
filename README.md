# Hunter MOV Converter

A simple command-line tool to convert MOV files to MP4 format.

## Installation

You can install this package directly from GitHub using uv:

```bash
uv pip install git+https://github.com/yourusername/hunter-mov-convert.git
```

Or if you've cloned the repository:

```bash
cd hunter-mov-convert
uv pip install .
```

## Usage

After installation, you can use the `hunter-converter` command to convert MOV files:

```bash
hunter-converter /path/to/your/mov/folder
```

The tool will:
1. Create a new `mp4` subfolder in your input folder
2. Convert all MOV files in the input folder to MP4 format
3. Save the converted files in the `mp4` subfolder

## Requirements

- Python 3.8 or higher
- moviepy
- tqdm
