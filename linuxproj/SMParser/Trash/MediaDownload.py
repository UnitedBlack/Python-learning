import os, aiofiles, aiohttp, asyncio
from datetime import datetime

async def save_media(author, subname, url, post_type, img_count = 1):
    date_hms = datetime.today().strftime('%H-%M-%S')
    day = str(datetime.today().date())
    path = f"ImageDownload/temp/{subname}-{day}-{date_hms}"
    destination = f"{path}/{author}.png"
    
    if post_type == "image":
        os.mkdir(path)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(destination, mode='wb')
                    await f.write(await resp.read())
                    await f.close()
                    
    elif post_type == "gallery":
        os.mkdir(path)
        for count in range(img_count):
            destination = f"{path}/{author}{count}.png"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        f = await aiofiles.open(destination, mode='wb')
                        await f.write(await resp.read())
                        await f.close()
                        
    elif post_type == "video":
        path = f"VideoDownload/temp/{subname[2:]}-{day}-{date_hms}"
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
        for i in command: print(i)
        process = await asyncio.create_subprocess_exec(*command)
        await process.wait()