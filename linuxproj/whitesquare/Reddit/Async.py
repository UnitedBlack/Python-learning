import asyncio, os
from playwright.async_api import async_playwright
# from video_download import download_media
from Image.image_download import save_image_async

class RedditAsync():
    def __init__(self) -> None:
        super(RedditAsync, self).__init__()
        self.previous_titles = {}
       
    async def __add_id_to_file(self, i, post_title_id):
        self.previous_titles.setdefault(self.current_subreddit[2:], set()).add(post_title_id)
        with open(f'Reddit/Subs/{self.links[i].split("/")[-2]}.txt', 'a') as f:
            f.write(f"{post_title_id}\n")
            f.close()
        
        
    async def __download_image_post(self, image_post, i, post_title_id):
        for current_post in image_post:
            if post_title_id not in self.previous_titles.get(self.current_subreddit[2:], set()):
                url = await current_post.get_attribute("content-href")
                # subreddit_id = current_post.get_attribute("subreddit-id")
                author = await current_post.get_attribute("author")
                await save_image_async(image_url=url, name=author, subname=author)
                print(f"Новый post-title: {post_title_id} {self.subreddit_name}")
                self.previous_titles.setdefault(self.current_subreddit[2:], set()).add(post_title_id)
                with open(f'subs/{self.links[i].split("/")[-2]}.txt', 'a') as f:
                    f.write(f"{post_title_id}\n")
            else: continue
            
        
    async def __parse_video_post(self, video_post, i):
        for current_post in video_post:
            #post_text
            post_title_id = await current_post.eval_on_selector('xpath=ancestor::shreddit-post', 'node => node.getAttribute("id")')
            self.subreddit_name = await current_post.eval_on_selector('xpath=ancestor::shreddit-post', 'node => node.getAttribute("subreddit-prefixed-name")')
            
            #эту ёбань вниз перетащить


    async def __parse_image_post(self, image_post, i):
        for current_post in image_post:
            ...
            
    
    
    # async def __parse_text_post(self, text_post, author):
        # print("Im here")
        # for current_post in text_post:
        #     txt = await text_post.get_attribute("post-title")
        #     with open(f"{author}.txt", "w", encoding="utf-8") as file:
        #         file.write(txt)
            
        
        
    async def __get_subreddit_name(self, page):
        what_is_current_subreddit = await page.query_selector('div[class="font-bold text-[18px]"]')
        self.current_subreddit = await what_is_current_subreddit.text_content()


    async def __create_file_with_sub_name(self):
        for subreddit in self.links:
            part = subreddit.split('/')
            self.subreddit_name = part[-2]
            self.subs_list.append(self.subreddit_name)

            if os.path.exists(f'Reddit/Subs/{self.subreddit_name}.txt'):
                with open(f'Reddit/Subs/{self.subreddit_name}.txt', 'r') as f:
                    self.previous_titles[self.subreddit_name] = set(line.strip() for line in f.readlines())
            else:
                print(f"Creating new file {self.subreddit_name}")
                with open(f'Reddit/Subs/{self.subreddit_name}.txt', 'w') as f:
                        f.write("")


    async def main(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            self.pages = []
            self.subs_list = []
            
            for link in self.links:
                context = await browser.new_context()
                page = await context.new_page()
                await page.goto(link)
                self.pages.append(page)
                
            await self.__create_file_with_sub_name()
            

            # потом вкорячить функцию, но оно багует если что
            while True:
                for i, page in enumerate(self.pages):
                    reddit_posts = await page.query_selector_all('shreddit-post')
                    await self.__get_subreddit_name(page=page)
                    
                    for reddit_post in reddit_posts: 
                        post_type = await reddit_post.get_attribute("post-type")
                        feed_index = await reddit_post.get_attribute("feedindex")
                        post_title_id = await reddit_post.get_attribute("id")
                        author = await reddit_post.get_attribute("author")
                        
                        if feed_index == "0":
                            continue
                        elif post_type == "video":
                            video_post = await page.query_selector_all('shreddit-player')
                            await self.__parse_video_post(video_post, i)
                        # elif post_type == "image":
                        #     image_post = await page.query_selector_all('shreddit-post')
                        #     await self.__download_image_post(image_post, i, post_title_id)
                        # elif post_type == "gallery":
                        #     print("gallery found")
                        # elif post_type == "text":
                        #     text_post = await page.query_selector_all('shreddit-post')
                        #     await self.__parse_text_post(text_post, author)
                        # else:
                        #     print("Unable to parse")
                        #     print(post_type)
                            
                            # опять дрисня не обновляет страницы

                        if post_title_id not in self.previous_titles.get(self.current_subreddit[2:], set()):
                            print(f"Новый post-title: {self.subreddit_name}")
                            await self.__add_id_to_file(i, post_title_id)

                    
                    with open(f'Reddit/Subs/{self.current_subreddit[2:]}.txt', 'r', encoding='utf-8') as file:
                        sub_file_content = file.read() # нельзя эту логику убирать, она нужна на каждой итерации
                        
                    if self.subreddit_name[2:] not in self.previous_titles:
                        self.previous_titles[self.subreddit_name[2:]] = set(line.strip() for line in sub_file_content.split("\n"))
                        
                # добавить еще чтобы пиздил ссылки, чтобы пиздил галерею, чтобы переводил текст
                await asyncio.sleep(10)
                for page in self.pages: await page.reload()
                

    async def first_load(self, links: list):
        self.links = links
        await self.main()
#    "https://www.reddit.com/r/AskReddit/"  "https://www.reddit.com/r/legostarwars/",
urls = ["https://www.reddit.com/r/maintheater/", "https://www.reddit.com/r/secondtheater/",]

if __name__ == "__main__":
    reddit_async = RedditAsync()
    asyncio.run(reddit_async.first_load(urls))