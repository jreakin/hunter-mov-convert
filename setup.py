from setuptools import setup, find_packages

setup(
    name="hunter-mov-convert",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "moviepy>=1.0.3",
        "tqdm>=4.65.0",
    ],
    python_requires=">=3.8",
    author="John Eakin",
    description="A tool to convert MOV files to MP4 format",
) 