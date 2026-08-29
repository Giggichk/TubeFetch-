import os
from yt_dlp import YoutubeDL
from src.verifications import check_correct_link, check_exist_link
from src.downloads import download, change_format, change_path


def main():

    ydl_opts = {
        "cookiesfrombrowser": ("firefox",)
    }

    url = input("Enter the link: ")

    if check_correct_link(url):
        is_avaible, info = check_exist_link(url, ydl_opts)
        if is_avaible:
            print("Video is accessible")
            format = input("Please, enter the format: ")
            ydl_opts.setdefault("format", change_format(format))

            path = input("Please, enter the path: ")
            valid_path = change_path(path)
            if valid_path:
                full_output_template = os.path.join(str(valid_path), "%(title)s.%(ext)s")
                ydl_opts.setdefault("outtmpl", full_output_template)

                run = input("Do you want to run? (y/n): ").lower()
                if run == "y":
                    download(url, ydl_opts)
            else:
                print("Path is not valid")
    else:
        print("link is invalid")


if __name__ == "__main__":
    main()



