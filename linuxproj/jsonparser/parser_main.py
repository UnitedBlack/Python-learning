import os, json, time, aiohttp, asyncio, aiofiles
from datetime import datetime
from media_download import download_video


class RedditTG:
    def __init__(self) -> None:
        self.temp_files_folder = "sub_temp_files/"
        self.data = []
        self.tg = []


    async def prepare_and_download_video_folder(self, video_url, post_id):
        hms_time = f"video_{datetime.today().strftime('%H-%M-%S')}"
        folder = os.path.join(self.temp_files_folder, self.subreddit_name, hms_time)
        os.makedirs(folder, exist_ok=True)
        filename = f"{post_id}.mp4"
        return await download_video(video_url, folder, filename)


    async def post_id_exists(self, post_id):
        try:
            with open(self.subreddit_json_file, "r") as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
            self.data = []

        if post_id in self.data:
            return True
        else:
            self.data.append(post_id)
            with open(self.subreddit_json_file, "w") as file:
                json.dump(self.data, file)
            return False

    async def process_reddit_post(self, post):
        link_flair_text = post['data']['link_flair_text']
        if link_flair_text == "Mod Post ":
            return

        post_id = post['data']['id']
        title = post['data']['title']
        post_url = post['data']['url']
        
        is_exist = await self.post_id_exists(post_id)
        if not is_exist:
            data = {
                'post_url': post_url,
                'subreddit_name': self.subreddit_name,
                'post_text': title,
                'media_type': None,
                'media_url': None,
                'video_path': None,
            }

            if "i.redd.it/" in post_url:
                data['media_type'] = "image"
                data['media_url'] = post_url

            elif "www.reddit.com/gallery/" in post_url:
                data['media_type'] = "gallery"
                gallery_dict = []
                gallery_media_id = [item['media_id']
                                    for item in post['data']['gallery_data']['items']]
                for meta in gallery_media_id:
                    metadata = post['data']['media_metadata'][meta]['s']['u']
                    clear_url = metadata.replace("amp;", "")
                    gallery_dict.append(clear_url)

                data['media_url'] = gallery_dict

            elif "v.redd.it/" in post_url:
                if post['data'].get('crosspost_parent_list') and 'reddit_video' in post['data']['crosspost_parent_list'][0]['media']:
                    video_url = post['data']['crosspost_parent_list'][0]['media']['reddit_video']['dash_url']

                elif post['data'].get('media') and 'reddit_video' in post['data']['media']:
                    video_url = post['data']['media']['reddit_video']['dash_url']
                    
                video_path = await self.prepare_and_download_video_folder(video_url, post_id)

                data['media_type'] = "video"
                data['media_url'] = video_url
                data['video_path'] = video_path

            elif "i.imgur.com" in post_url:
                if "gifv" in post_url:
                    print('gif')

            elif "youtube.com" in post_url or "youtu.be" in post_url:
                data['media_type'] = "video"
                data['media_url'] = post_url

            elif "old.reddit.com/r/" in post_url:
                data['media_type'] = "text"
                data['media_url'] = post_url

            else:
                print(f"Unknown URL: {post_url}")
            
            if data["media_type"]:
                self.tg.append(data)

    async def create_default_folders(self):
        main_folder = "sub_temp_files"
        subreddit_folder = os.path.join(main_folder, self.subreddit_name)
        os.makedirs(subreddit_folder, exist_ok=True)

    async def main(self, url):
        print(datetime.today().strftime('%H-%M-%S'))
        url_reddit = url
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url_reddit, headers=self.headers) as response:
                data_text = await response.text()
                data = json.loads(data_text)

        self.subreddit_name = data['data']['children'][0]['data']["subreddit_name_prefixed"][2:]
        await self.create_default_folders()
        self.subreddit_json_file = f"{self.temp_files_folder}{self.subreddit_name}/{self.subreddit_name}.json"

        if os.path.exists(self.temp_files_folder):
            if not os.path.isfile(self.subreddit_json_file):
                with open(self.subreddit_json_file, "w", encoding="utf-8") as file:
                    file.write("")
                    self.existing_data = []

        tasks = [self.process_reddit_post(post) for post in data['data']['children']]
        await asyncio.gather(*tasks)

        if self.tg != []:
            async with aiofiles.open(f"Results/{datetime.today().strftime('%H-%M-%S')}.json", "w") as file:
                await file.write(json.dumps(self.tg))
                await file.close()
                return f"Results/{datetime.today().strftime('%H-%M-%S')}.json"
        else: 
            return False


# if __name__ == "__main__":
#     while True:
#         urls = [
#             # "https://old.reddit.com/r/legostarwars/.json",
#             "https://old.reddit.com/r/yesyesyesyesno/.json",
#             # "https://old.reddit.com/r/maintheater/.json",
#             # "https://old.reddit.com/r/secondtheater/.json",
#             # "https://old.reddit.com/r/askreddit/.json",
#             # "https://old.reddit.com/r/gif/.json",
#             # "https://old.reddit.com/r/youtubehaiku/.json"
#         ]
#         red = RedditTG()

#         async def main():
#             tasks = [red.main(url) for url in urls]
#             bred = await asyncio.gather(*tasks)
#         asyncio.run(main())
#         time.sleep(10)