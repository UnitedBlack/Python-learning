import subprocess


def download_video(url):
    try:
        path = f"editor/temp/{url.replace('https://youtube.com/watch?v=', '')}.mp4"
        command = ["yt-dlp", "-o", path, url]
        subprocess.run(command)
        return path
    except Exception as e:
        print(e)


# path = f"editor/temp/{name}.mp4"