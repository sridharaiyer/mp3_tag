from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os
import argparse

# print(EasyID3.valid_keys.keys())

parser = argparse.ArgumentParser()
parser.add_argument("--genre", action="store", help='Genre of all the MP3 files in this directory')
args = parser.parse_args()

if args.genre is None:
    print('Need to specify a genre:\n', parser.print_help())
    exit(1)

filenames = [f for f in os.listdir(os.getcwd()) if f.endswith('.mp3')]

current_folder_path, current_folder_name = os.path.split(os.getcwd())
print('current_folder_path: ', current_folder_path)
print('current_folder_name: ', current_folder_name)

for file_name in filenames:
    audio = MP3(file_name, ID3=EasyID3)
    print('Setting the title of file {} as the same'.format(file_name))
    audio["title"] = file_name
    print('Setting the album of file {} to the current folder name - {}'.format(file_name, current_folder_name))
    audio["album"] = current_folder_name
    print('Setting the genre of file {} tas - {}'.format(file_name, args.genre))
    audio["genre"] = args.genre
    audio.save()
