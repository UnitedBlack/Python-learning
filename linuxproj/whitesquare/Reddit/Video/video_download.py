import os, asyncio
from datetime import datetime


async def download_video_async(author, subname, url):
    date_hms = datetime.today().strftime('%H-%M-%S')
    day = str(datetime.today().date())
    path = f"Video/{subname}-{day}-{date_hms}"
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
        path + "/" + author + "_" + date + ".mp4",
        ]

    process = await asyncio.create_subprocess_exec(*command)
    await process.wait()
    
    
asyncio.run(download_video_async(author="bebra", url="https://packaged-media.redd.it/e9yu4v41d7rb1/pb/m2-res_854p.mp4?m=DASHPlaylist.mpd&v=1&e=1696028400&s=edd805d9fa39526e1a98e290dd324234643cfd9e#t=0"))
