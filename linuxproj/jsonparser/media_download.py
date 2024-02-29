import aiohttp, aiofiles, asyncio, json, time, os
from datetime import datetime


async def download_gallery(url, folder, filename, title):
    print('='*40)
    print(f"Downloading gallery image {filename}")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    destination = os.path.join(folder, filename)
                    async with aiofiles.open(destination, mode='wb') as f:
                        await f.write(await resp.read())
    except Exception as e:
        print(f"Error downloading gallery image: {url}")
        print(e)

    return destination


async def download_image(post, url, folder, filename, title):
    print('='*40)
    print(f"Downloading {filename}")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    destination = os.path.join(folder, filename)
                    async with aiofiles.open(destination, mode='wb') as f:
                        await f.write(await resp.read())
    except Exception as e:
        print(f"Error downloading image: {url}")
        print(e)
    data = {
        'post_url': post['data']['url'],
        'subreddit_name': post['data']['subreddit'],
        'post_text': title,
        'media_type': "image",
        'media_path': destination
    }
    return data

# media_type поменя
async def download_text(post, title, folder, author):
    timestamp = int(time.time())
    filename = f"{author}_{timestamp}.txt"
    file_path = os.path.join(folder, filename)
    data = {
        'post_url': post['data']['url'],
        'subreddit_name': post['data']['subreddit'],
        'post_text': title,
        'media_type': "text",
        'media_path': file_path
    }
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(title)
        
    return data


async def download_video(url, folder, filename):
    print('='*30)
    print(f"Downloading {filename}")
    destination = os.path.join(folder, filename)
    command = [
        "ffmpeg",
        "-i",
        url,
        "-c",
        "copy",
        "-bsf:a",
        "aac_adtstoasc",
        "-loglevel",
        "quiet",
        "-hide_banner",
        destination]
    try:
        process = await asyncio.wait_for(
            asyncio.create_subprocess_exec(
                *command,
                stdout=asyncio.subprocess.PIPE,  # Redirect stdout
                stderr=asyncio.subprocess.PIPE   # Redirect stderr
            ),
            timeout=30
        )
        stdout, stderr = await process.communicate()  # Read stdout, stderr
        if stdout:
            print(f"[stdout]\n{stdout.decode()}")
        if stderr:
            print(f"[stderr]\n{stderr.decode()}")
    except asyncio.TimeoutError:
        print(f"Timeout while processing video: {url}")
    except Exception as e:
        print(f"Error while processing video: {url}")
        print(e)
    return destination


# ffmpeg -i "" -c copy -bsf:a aac_adtstoasc -hide_banner video.mp4
# https://v.redd.it/d7pgf85jz0ub1/DASHPlaylist.mpd?a=1700082827%2CNzMyYmM5NjgyMzU3MDljMWE1NDZiYmFiZDc2ODg1NjZiZWY5NTQwYTI4NDg3ZTkwMTQ5NjUwNGIxZTdiNWRjOQ%3D%3D&amp;v=1&amp;f=sd