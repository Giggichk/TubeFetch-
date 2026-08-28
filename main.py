from yt_dlp import YoutubeDL
from src.verifications import check_correct_link, check_exist_link
from src.downloads import download


def main():

    ydl_opts = {
        "cookiesfrombrowser": ("firefox",)
    }

    url = input("Enter the link: ")

    if check_correct_link(url):
        is_avaible, info = check_exist_link(url, ydl_opts)
        if is_avaible:
            print("Video is accessible")
    else:
        print("link is invalid")


if __name__ == "__main__":
    main()



