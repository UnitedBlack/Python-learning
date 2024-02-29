import asyncio
import aiohttp
import os
import json
from datetime import datetime
from lxml import etree
from Trash.MediaDownload import save_media

class Reddit():
    def __init__(self) -> None:
        self.HMS_TIME = datetime.today().strftime('%H-%M-%S')
        self.HM_TIME = datetime.today().strftime('%H-%M')
        self.MODHM_TIME = datetime.today().strftime('d%d-m%m-H%H-M%M')
        self.SUBS_TEXT_PATH = "Subs/"
        self.sub_names = []
        self.existing_data = str


    async def __write_to_file(self, subname, data):
        path = f"{self.SUBS_TEXT_PATH}{subname[2:]}.json"
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as file:
                self.existing_data = json.load(file)
            if self.existing_data == data:
                print("Equal")
            else:
                print("Adding data")
                with open(path, "w", encoding="utf-8") as file:
                    json.dump(data, file)
        else:
            print(f"Can't find file with subname {subname}")


    async def __parse_page(self, html):
        shreddit_posts = html.xpath('//shreddit-post')
        
        for post in shreddit_posts:
            video_element = post.find("video")
            print(video_element)
            subname = post.attrib["subreddit-prefixed-name"]
            post_types = post.attrib["post-type"]
            post_ids = [post.attrib["id"] for post in shreddit_posts]
            post_authors = post.attrib["author"]
            post_urls = post.attrib["content-href"]
            


            if post_types == "text" and post_ids != self.existing_data:
                print("text not in existing data")

            elif post_types != "text" and post_ids != self.existing_data:
                await save_media(author=post_authors, subname=subname, url=post_urls,
                        post_type=post_types, img_count=1)

        await self.__write_to_file(subname=subname, data=post_ids)
        await asyncio.sleep(15)


    async def __create_or_read_file_with_subname(self, subname):
        path = f"{self.SUBS_TEXT_PATH}{subname}.json"
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as file:
                self.existing_data = json.load(file)
                file.close()
        else:
            print(f"Creating file with subname {subname}")
            with open(path, "w", encoding="utf-8") as file:
                json.dump([], file)
                file.close()

    def __get_sub_name(self, html):
        sub_name = html.xpath('//shreddit-post[1]/@subreddit-prefixed-name')
        for name in sub_name:
            self.sub_names.append(name[2:])


    async def get_html(self, url):
        while True:
            print("Parsing")
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url) as response:
                    html = await response.text()
            for_clear_html = html.partition("<report-flow-provider")[2]
            clear_html = for_clear_html.partition('<span class="text-14">Home</span>')[0]
            tree = etree.HTML(clear_html)

            self.__get_sub_name(tree)
            for name in self.sub_names: await self.__create_or_read_file_with_subname(subname=name)
            await self.__parse_page(tree)


if __name__ == "__main__":
    parse = Reddit()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(parse.get_html("https://www.reddit.com/r/maintheater/"))
    loop.close()
