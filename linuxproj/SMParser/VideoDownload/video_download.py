import os, asyncio
from datetime import datetime


async def download_video_async(author, subname, url):
    date_hms = datetime.today().strftime('%H-%M-%S')
    day = str(datetime.today().date())
    path = f"VideoDownload/temp/{subname}-{day}-{date_hms}"
    os.mkdir(path)
    date = datetime.today().strftime('%M-%S')
    
    command = [
        "ffmpeg",
        "-i",
        url,
        "-c",
        "copy",
        "-bsf:a",
        "aac_adtstoasc",
        path + "/" + author + "_" + date + ".mp4",]
    process = await asyncio.create_subprocess_exec(*command)
    await process.wait()