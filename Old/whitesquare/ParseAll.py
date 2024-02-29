from playwright.sync_api import sync_playwright
from Video.video_download import download_media
from datetime import datetime
import time, sys, os


class TGBot():
    def __init__(self) -> None:
        pass


class ChatGPT():
    def __init__(self):
        pass
    
    
    def translate(self, text):
        print("Если текст на русском верни ту же строку")


class RedditParseAll():
    def __init__(self):
        super(RedditParseAll, self).__init__()
        GPT = ChatGPT()
        self.cycle = 0

    
    def __scroll(self, count:int):
        for scroll in range(count):
            post = self.page.query_selector_all('shreddit-post')
            self.page.evaluate('(element) => { element.scrollIntoView(); }', post[-1])
            self.page.wait_for_timeout(1500)
            # self.page.wait_for_selector('shreddit-post')
    
    def __parse_new_content(self):
        ...

    def __parse_page_all_content(self, url, download="n", iteration=10):
        self.page.goto(url)
        if download == "y":
            self.date = datetime.today().strftime('%H-%M-%S')
            self.day = str(datetime.today().date())
            self.mkdir = f"Video/{self.day}-{self.date}"
            os.mkdir(self.mkdir)
            
        self.page.wait_for_selector('shreddit-post')
        self.__scroll(1)
        video = self.page.query_selector_all('shreddit-player')
        
        try:
            for current_video in video:
                self.cycle += 1
                video_url = current_video.get_attribute('src')
                post_title_from_parent = current_video.eval_on_selector('xpath=ancestor::shreddit-post', 'node => node.getAttribute("post-title")')
                post_author_from_parent = current_video.eval_on_selector('xpath=ancestor::shreddit-post', 'node => node.getAttribute("author")')
                # post_id_from_parent = current_video.eval_on_selector('xpath=ancestor::shreddit-post', 'node => node.getAttribute("id")')
                # post_type_from_parent = current_video.eval_on_selector('xpath=ancestor::shreddit-post', 'node => node.getAttribute("post-type")')
                print(post_title_from_parent)
                
                if download == "y":
                    if self.cycle == 1: print("Downloading video")
                    time.sleep(1)
                    download_media(self.mkdir, post_author_from_parent, video_url)
                    
        finally: print("Done")
        
        
# сделать парсинг разных страниц, то есть тут должен быть список
# чето типа for url in list_of_urls self.page.goto
      
    def load_page(self, url="", parse_all="y"):
        with sync_playwright() as playwright:
            browser = playwright.firefox.launch(headless=False)
            self.context = browser.new_context()
            self.page = self.context.new_page()
            if parse_all == "y":
                self.__parse_page_all_content(url=url)
                

    
    
if __name__ == "__main__":
    parser_reddit = RedditParseAll()
    parser_reddit.load_page(url="https://www.reddit.com/r/yesyesyesyesno/", parse_all="y")

# первым делом делаю реакцию на новый пост
# потом делаю асинхронный мониторинг всех ссылок на новые посты
# потом делаю асинх вызов ффмпег, гпт
# потом асинх вызов тг