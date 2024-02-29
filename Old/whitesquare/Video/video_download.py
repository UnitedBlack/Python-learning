import subprocess
from datetime import datetime

def download_media(path, author, url):
    date = datetime.today().strftime('%M-%S')
    command = [
        "ffmpeg",
        "-i",
        url,
        "-c",
        "copy",
        "-bsf:a",
        "aac_adtstoasc",
        path + "/" + author + "_" + date + ".mp4",
        ]
    subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)