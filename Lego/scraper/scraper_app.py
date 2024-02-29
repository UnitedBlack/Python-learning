import requests
from lxml import html
import g4f

# jaysbrickblog = requests.get(url="https://jaysbrickblog.com/lego-news/")
# # with open("site_data.html", "w", encoding="utf-8") as file:
# #     file.write(a.text)

# html_string = jaysbrickblog.text
# root = html.fromstring(html_string)

# parse = root.xpath('//a[@class="alignnone"]')[0].get("href")
# for i, elem in enumerate(parse):
#     print(i, elem.get("href"))

jaysbrickblog_page = requests.get(
    url="https://jaysbrickblog.com/news/lego-marvel-january-2024-sets-include-the-return-of-lego-x-men/"
)
html_string = jaysbrickblog_page.text
root = html.fromstring(html_string)
parse2 = root.xpath('//div[@class="entry-content"]')

for parse in parse2:
    text = parse.text_content()
    text = " ".join(text.split())
# print(text)

# ChatgptAi
# Geekgpt
response = g4f.ChatCompletion.create(
    provider=g4f.Provider.Hashnode,
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": f"Переведи это на русский язык в свободной форме как будто общаешься с другом и разбей на логические абзацы {text}",
        }
    ],
)  # Alternative model setting

print(response)

# g4f.Provider.ChatgptAi
g4f.Provider.Hashnode
g4f.Provider.MyShell
g4f.Provider.NoowAi
g4f.Provider.OpenaiChat
g4f.Provider.Theb
g4f.Provider.Vercel
g4f.Provider.You
g4f.Provider.Yqcloud
g4f.Provider.Acytoo
g4f.Provider.Aibn
g4f.Provider.Ails
g4f.Provider.Chatgpt4Online
g4f.Provider.ChatgptDemo
g4f.Provider.ChatgptDuo
g4f.Provider.ChatgptFree
g4f.Provider.ChatgptLogin
g4f.Provider.Cromicle
g4f.Provider.GptGod
g4f.Provider.Opchatgpts
g4f.Provider.Ylokh
