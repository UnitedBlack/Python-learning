import os, aiofiles, aiohttp, asyncio
from datetime import datetime


async def save_image_async(author, subname, url, post_type, img_count = 1):
    date_hms = datetime.today().strftime('%H-%M-%S')
    day = str(datetime.today().date())
    path = f"ImageDownload/temp/{subname}-{day}-{date_hms}"
    os.mkdir(path)
    destination = f"{path}/{author}.png"
    
    if post_type == "image":
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(destination, mode='wb')
                    await f.write(await resp.read())
                    await f.close()
                    
    elif post_type == "gallery":
        for count in range(img_count):
            destination = f"{path}/{author}{count}.png"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        f = await aiofiles.open(destination, mode='wb')
                        await f.write(await resp.read())
                        await f.close()
                        
asyncio.run(save_image_async(url="https://www.reddit.com/gallery/16zjulf", author="deb", subname="legostarwars", post_type="gallery", img_count=2))