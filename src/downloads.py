import os
import pathlib
from yt_dlp import YoutubeDL


def download(url, options):
    with YoutubeDL(options) as ydl:
         ydl.download(url)


def change_format(quality):
    match quality:
        case "maxquality":
            return r'bestvideo+bestaudio/best'
        case "fullhd":
            return r'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]/best'
        case "hd":
            return r'bestvideo[height<=720]+bestaudio/best[height<=720]/best'
        case "minquality":
            return r'bestvideo[height<=480]+bestaudio/best[height<=480]/worst'
        case "onlyaudio":
            return r'bestaudio/best'
        case _:
            return None


def change_path(dir):
    path = pathlib.Path(dir)

    if path.is_absolute():
        if path.is_dir() and path.exists():
            return path
        else:
            return False
    else:
        home_dir = pathlib.Path.home()
        current_project_dir = pathlib.Path.cwd()

        target_name = path.name

        for root, dirs, files in os.walk(home_dir):
            root_path = pathlib.Path(root)
            if current_project_dir in root_path.parents or root_path == current_project_dir:
                continue

            if target_name in dirs:
                potential_path = root_path / target_name

                if potential_path.match(f"*{path}"):
                    return potential_path.resolve()

        return False