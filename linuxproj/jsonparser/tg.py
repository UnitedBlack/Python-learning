import parser_main
import json
import time
import asyncio
import aiofiles
import logging
import sys
import os
import shutil
import re

from gpt import gpt_translate
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile
from aiogram.utils.markdown import hbold
from aiogram.types import InputMediaPhoto

from aiogram.methods import SendMediaGroup
from aiogram.utils.media_group import MediaGroupBuilder

# кнопки для перевода

TOKEN = "6616429815:AAHlnRicZwp7C8P9JUxlN-pBC7JE16IwTxE"
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
me = ["333253716", "1074422484"]
urls = [
    "https://old.reddit.com/r/legostarwars/.json",
    # "https://old.reddit.com/r/yesyesyesyesno/.json",
    "https://old.reddit.com/r/maintheater/.json",
    # "https://old.reddit.com/r/secondtheater/.json",
    # "https://old.reddit.com/r/askreddit/.json",
]

video_paths = []

async def send_posts(url, reddit):
    # await bot.send_video(
    #     chat_id=me[0],
    #     video=FSInputFile("sub_temp_files/yesyesyesyesno/video_22-58-57/178ah9p.mp4")
    #     )
    path = await reddit.main(url)
    if path:
        async with aiofiles.open(path, mode='r') as file:
            data = await file.read()
            parse_result = json.loads(data)
            
        for post in parse_result:
            post_url = post['post_url']
            subreddit_name = post['subreddit_name'].capitalize()
            
            text_of_post_text = post['post_text']
            print(text_of_post_text)
            text_inside_at = await gpt_translate(text_of_post_text)
            print(text_inside_at)
            re_text = re.search(r'@(.+?)@', text_inside_at)
            translated_text = re_text.group(1)
            # сделать try except тут и доделать гпт перевод
            post_type = post['media_type']
            media_url = post['media_url'] # пикчи, галерея
            video_path = post['video_path']
            
            text = f"{translated_text}\n{post_url}\n#{subreddit_name}"
            
            if post_type == "text":
                for user in me:
                    await bot.send_message(chat_id=user, text=text)
                
            elif post_type == "video":
                for user in me:
                    await bot.send_video(
                        chat_id=user,
                        video=FSInputFile(video_path),
                        caption=text)
                    if video_paths == []:
                        video_paths.append(video_path)
            
            elif post_type == "image":
                for user in me:
                    await bot.send_photo(
                        chat_id=user,
                        photo=media_url,
                        caption=text)
                        
            elif post_type == "gallery":
                media_group = MediaGroupBuilder(caption=text)
                for pic in media_url:
                    media_group.add(type="photo", media=pic)
                for user in me:
                    await bot.send_media_group(chat_id=user, media=media_group.build())
        return path


async def main():
    tasks = []
    for url in urls:
        reddit = parser_main.RedditTG()
        tasks.append(send_posts(url, reddit))
    results = await asyncio.gather(*tasks)
    
    # if video_paths != []:
    #     video_folder = os.path.dirname(video_paths[0])
    #     shutil.rmtree(video_folder)
        
    for result in results:
        if result:
            os.remove(result)
            
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
# data = [
#   {
#     "post_url": "https://i.redd.it/yeivaow3plub1.jpg",
#     "subreddit_name": "legostarwars",
#     "post_text": "20 years in the making, never was able to afford an AT-TE as a kid, did get the turbo tank for Christmas once… here I am now though. “Marked nsfw because of water pipe, yes I live in a legal state and loving it”",
#     "media_type": "image",
#     "media_url": "https://i.redd.it/yeivaow3plub1.jpg"
#     },
#     {
#     "post_url": "https://www.reddit.com/gallery/1799bry",
#     "subreddit_name": "legostarwars",
#     "post_text": "Someone take my debit card away",
#     "media_type": "gallery",
#     "media_url": [
#         "https://preview.redd.it/bucyved77lub1.jpg?width=2316&format=pjpg&auto=webp&s=d0dc6f34c442b0a73770d44ed1b870c0267b1c0a",
#         "https://preview.redd.it/w5nhzcd77lub1.jpg?width=3024&format=pjpg&auto=webp&s=79b1f1a23d77e8a5040a9e934f7eb72a49222a30",
#         "https://preview.redd.it/i222igd77lub1.jpg?width=1242&format=pjpg&auto=webp&s=6660690e6662cb3ccb5475a72fe10ff2f67f97b4"
#     ]
#     },
#   {
#     "post_url": "https://v.redd.it/byiyc19wgytb1",
#     "subreddit_name": "yesyesyesyesno",
#     "post_text": "Yesyesyesyesno ",
#     "media_type": "video",
#     "media_url": "https://v.redd.it/byiyc19wgytb1/DASH_1080.mp4?source=fallback"
#   },
# ]