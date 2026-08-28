from yt_dlp import YoutubeDL


def download(url, options):
    with YoutubeDL(options) as ydl:
         ydl.download(url)



