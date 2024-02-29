import aiohttp, aiofiles, asyncio, json, time, os
from datetime import datetime
from media_download import download_image, download_text, download_video, download_gallery

class RedditTG:
    def __init__(self) -> None:
        self.temp_files_folder = "sub_temp_files/"
        self.data = []
        self.tg = []
    
        
    async def post_id_exists(self, post_id):
        try:
            with open(self.subreddit_json_file, "r") as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.data = []
            
        if post_id in self.data:
            return True
        else:
            self.data.append(post_id)
            with open(self.subreddit_json_file, "w") as file:
                json.dump(self.data, file)
            return False
        
    
    async def procces_text_post(self, post, text_folder, title):
        download_text_res = await download_text(title, text_folder, post['data']['author'])
        self.tg.append(download_text_res)


    async def procces_gallery_post(self, author, date_hms_folder, gallery_urls: list, title):
        gallery_folder = os.path.join(date_hms_folder, "Gallery")
        os.makedirs(gallery_folder, exist_ok=True)
        
        author_folder = os.path.join(gallery_folder, author)
        os.makedirs(author_folder, exist_ok=True)
        dict_of = []
        
        for url in gallery_urls:
            clear_url = url.replace("amp;", "")
            filename = f"{url[24:37]}.jpg"
            download_gallery_res = await download_gallery(clear_url, author_folder, filename, title)
            self.tg.append(download_gallery_res)


    async def process_video_post(self, post, video_url, date_hms_folder, title):
        video_folder = os.path.join(date_hms_folder, "Video")
        os.makedirs(video_folder, exist_ok=True)
        filename = f"{post['data']['author']}_{post['data']['id']}.mp4"
        download_video_res = await download_video(video_url, video_folder, filename, title)
        self.tg.append(download_video_res)


    async def process_image_post(self, post, date_hms_folder, title):
        image_folder = os.path.join(date_hms_folder, "Image")
        os.makedirs(image_folder, exist_ok=True)
        filename = f"{post['data']['author']}_{post['data']['id']}.png"
        download_image_res = await download_image(post['data']['url'], image_folder, filename, title)
        self.tg.append(download_image_res)


    async def process_reddit_post(self, post, date_hms_folder):
        link_flair_text = post['data']['link_flair_text']
        if link_flair_text == "Mod Post ": 
            return
        
        post_id = post['data']['id']

        media_info = None
        title = post['data']['title']
        
        
        is_exist = await self.post_id_exists(post_id)
        if not is_exist:
            if "i.redd.it/" in post['data']['url']:
                await self.process_image_post(post, date_hms_folder, title)

            elif "www.reddit.com/gallery/" in post['data']['url']:
                gallery_dict = []
                gallery_media_id = [item['media_id'] for item in post['data']['gallery_data']['items']]
                author = post['data']['author']
                for meta in gallery_media_id:
                    metadata = post['data']['media_metadata'][meta]['s']['u']
                    gallery_dict.append(metadata)
                    
                await self.procces_gallery_post(author=author, date_hms_folder=date_hms_folder, 
                                                gallery_urls=gallery_dict, title=title)

            elif "v.redd.it/" in post['data']['url']:
                if post['data'].get('crosspost_parent_list') and 'reddit_video' in post['data']['crosspost_parent_list'][0]['media']: 
                    video_url = post['data']['crosspost_parent_list'][0]['media']['reddit_video']['fallback_url']
                
                elif post['data'].get('media') and 'reddit_video' in post['data']['media']:
                    video_url = post['data']['media']['reddit_video']['fallback_url']
                    
                await self.process_video_post(post=post, video_url=video_url, 
                                              date_hms_folder=date_hms_folder, title=title)
                
            elif "i.imgur.com" in post['data']['url']:
                if "gifv" in post['data']['url']:
                    gifv_url = post['data']['url']
                    video_url = gifv_url.replace("gifv", "mp4")
                    await self.process_video_post(post=post, video_url=video_url, 
                                                  date_hms_folder=date_hms_folder, title=title)

            elif "old.reddit.com/r/" in post['data']['url']:
                text_folder = os.path.join(date_hms_folder, "Text")
                os.makedirs(text_folder, exist_ok=True)
                await self.procces_text_post(post=post, text_folder=text_folder, title=title)

            else:
                print(f"Unknown URL: {post['data']['url']}")

    async def create_default_folders(self):
        date_hms = datetime.today().strftime('%H-%M-%S')

        main_folder = "sub_temp_files"  
        subreddit_folder = os.path.join(main_folder, self.subreddit_name)
        os.makedirs(subreddit_folder, exist_ok=True)

        date_hms_folder = os.path.join(subreddit_folder, date_hms)
        os.makedirs(date_hms_folder, exist_ok=True)
    
        return date_hms_folder


    async def main(self):
        url_reddit = "https://old.reddit.com/r/legostarwars/.json"
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"}

        async with aiohttp.ClientSession() as self.session:
            async with self.session.get(url_reddit, headers=headers) as response:
                data_text = await response.text()
                data = json.loads(data_text)

        self.subreddit_name = data['data']['children'][0]['data']["subreddit_name_prefixed"][2:]
        date_hms_folder = await self.create_default_folders()
        self.subreddit_json_file = f"{self.temp_files_folder}{self.subreddit_name}/{self.subreddit_name}.json"
        
        if os.path.exists(self.temp_files_folder):
            if not os.path.isfile(self.subreddit_json_file):
                with open(self.subreddit_json_file, "w", encoding="utf-8") as file:
                    file.write("")
                    self.existing_data = []

        tasks = [self.process_reddit_post(post, date_hms_folder)
                for post in data['data']['children']]
        media_info_list = await asyncio.gather(*tasks)
        
        with open(f"{self.temp_files_folder}Results/{datetime.today().strftime('%H-%M-%S')}.json", "w") as file:
            json.dump(self.tg, file)
            

if __name__ == "__main__":
    red = RedditTG()
    asyncio.run(red.main())
    

# День 2
# доделать открытие жсон файла с каждым названием жсон саба - V
# и проверкой на айди постов, - X
# если есть то ничего не происходит, если нет то скачивается  - X
# сделать запись этих данных в жсон - X
# также если пост онли текст проверки - X
# в отдельном файле подключить тг бота - X
# сделать загрузку галереи - V
# сделать загрузку гиф - V

# День 3
# Доделать функцию чтения/записи айди файлов
# Переписать ее на асинхронную
# Доделать обработку текстовых постов
# Сделать гига пиздатый словарь {author_name: {"media_path"}} итд


# Использование aiohttp.ClientSession(): Вместо создания новой сессии для каждого запроса, 
# лучше создать одну сессию и использовать её для всех запросов. 
# Это увеличит производительность, поскольку сессия управляет пулом соединений 
# и может повторно использовать уже открытые соединения, 
# что уменьшает накладные расходы на установку нового соединения stackoverflow.com, stackoverflow.com.

            # media_info = {
            #     'media_type': "text",
            #     'media_path': os.path.join(text_folder, f"{post['data']['author']}.txt"),
            #     'post_text': post['data']['title']
            # }
            #         return {
            # 'media_type': "image",
            # 'media_path': os.path.join(image_folder, filename),
            # 'post_text': post['data']['title']}
            
            
            
        # if os.path.exists(filename):
        #     async with aiofiles.open(filename, mode='r') as f:
        #         data = await f.read()
        #     posts = json.loads(data)
        #     if post_id in posts:
        #         return True
        # return False
        