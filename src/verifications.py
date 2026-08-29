import re
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError, ExtractorError


def check_correct_link(url):
    pattern = r"^(https?://)?(www\.)?(youtube\.com/(watch\?v=|shorts/)|youtu\.be/)[\w-]{11}"
    return bool(re.match(pattern, url))


def check_exist_link(url, options=None):
    opts = {
        'extract_flat': False,
        'quiet': True,
        'no_warnings': True,
        **(options or {})
    }

    with YoutubeDL(opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return True, "Supported link"
        except (ExtractorError, DownloadError) as error:
            clean_error = str(error).replace("ERROR: ", "").strip()
            return False, clean_error