import aiofiles
import aiohttp
import asyncio
import os
from datetime import datetime


async def save_image_async(image_url, name, subname):
    date_hms = datetime.today().strftime('%H-%M-%S')
    day = str(datetime.today().date())
    path = f"Image/{subname}-{day}-{date_hms}"
    os.mkdir(path)
    
    destination = f"{path}/{name}.png"
    
    async with aiohttp.ClientSession() as session:
         async with session.get(image_url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(destination, mode='wb')
                await f.write(await resp.read())
                await f.close()
                