import asyncio
from playwright.async_api import async_playwright

class RedditAsync():
    def __init__(self) -> None:
        super(RedditAsync, self).__init__()
        self.previous_titles = {}

    async def main(self, links: list):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            self.pages = []
            
            for link in links:
                context = await browser.new_context()
                page = await context.new_page()
                await page.goto(link)
                self.pages.append(page)
                
            while True:
                for i, page in enumerate(self.pages):
                    video = await page.query_selector_all('shreddit-player')
                    what_is_current_subreddit = await page.query_selector('div[class="font-bold text-[18px]"]')
                    current_subreddit = await what_is_current_subreddit.text_content()
                    
                    with open(f'subs/{current_subreddit[2:]}.txt', 'r', encoding='utf-8') as file:
                        sub_file_content = file.read()
                        self.previous_titles[current_subreddit[2:]] = set(sub_file_content.split("\n"))
    
                    for current_video in video:
                        post_title_id = await current_video.eval_on_selector('xpath=ancestor::shreddit-post', 'node => node.getAttribute("id")')
                        subreddit_name = await current_video.eval_on_selector('xpath=ancestor::shreddit-post', 'node => node.getAttribute("subreddit-prefixed-name")')
                        
                        if post_title_id not in self.previous_titles.get(current_subreddit[2:], set()):
                            print(f"Новый post-title: {post_title_id} {subreddit_name}")
                            self.previous_titles.setdefault(current_subreddit[2:], set()).add(post_title_id)
                            with open(f'subs/{links[i].split("/")[-2]}.txt', 'a') as f:
                                f.write(f"{post_title_id}\n")

                await asyncio.sleep(10)

    async def first_load(self, links: list):
        await self.main(links)

urls = ["https://www.reddit.com/r/maintheater/", "https://www.reddit.com/r/secondtheater/"]

if __name__ == "__main__":
    reddit_async = RedditAsync()
    asyncio.run(reddit_async.first_load(urls))

