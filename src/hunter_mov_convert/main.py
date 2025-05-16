import argparse
from pathlib import Path
from moviepy import VideoFileClip
from tqdm import tqdm


class MovieFolder:
    def __init__(self, folder_path: Path | str):
        self.folder_path = Path(folder_path)
        self.mp4_folder_path = self.folder_path / 'mp4'
        self.mp4_folder_path.mkdir(exist_ok=True)

    def convert_mov_to_mp4(self, mov_path: Path | str):
        _mov_path = Path(mov_path)
        if not _mov_path.suffix == '.mov':
            print(f'{_mov_path} is not a MOV file, skipping...')
            return
        _mp4_path = self.mp4_folder_path / _mov_path.name
        try:
            clip = VideoFileClip(_mov_path)
            clip.write_videofile(_mp4_path, codec='libx264')
        except Exception as e:
            print(f'Error converting {_mov_path} to MP4: {e}')

    def read_folder(self):
        _mov_files = self.folder_path.glob('*.mov')
        for _mov_file in tqdm(_mov_files, desc='Converting MOV files to MP4'):
            self.convert_mov_to_mp4(_mov_file)
        print(f'Converted {len(list(self.mp4_folder_path.glob("*.mp4")))} MOV files to MP4')


def main():
    parser = argparse.ArgumentParser(description='Convert MOV files to MP4')
    parser.add_argument('folder_path', type=str, help='The path to the folder containing the MOV files')
    args = parser.parse_args()
    movie_folder = MovieFolder(args.folder_path)
    movie_folder.read_folder()


if __name__ == '__main__':
    main()