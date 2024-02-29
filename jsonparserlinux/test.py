import g4f, asyncio

_providers = [
g4f.Provider.Acytoo,
g4f.Provider.Aichat,
g4f.Provider.Ails,
g4f.Provider.AiService,
g4f.Provider.AItianhu,
g4f.Provider.Aivvm,
g4f.Provider.Bard,
g4f.Provider.Bing,
g4f.Provider.ChatBase,
g4f.Provider.ChatgptAi,
g4f.Provider.ChatgptLogin,
g4f.Provider.CodeLinkAva,
g4f.Provider.DeepAi,
g4f.Provider.DfeHub,
g4f.Provider.EasyChat,
g4f.Provider.Forefront,
g4f.Provider.GetGpt,
g4f.Provider.GptGo,
g4f.Provider.H2o,
g4f.Provider.HuggingChat,
g4f.Provider.Liaobots,
g4f.Provider.Lockchat,
g4f.Provider.Opchatgpts,
g4f.Provider.OpenaiChat,
g4f.Provider.OpenAssistant,
g4f.Provider.PerplexityAi,
g4f.Provider.Raycast,
g4f.Provider.Theb,
g4f.Provider.Vercel,
g4f.Provider.Vitalentum,
g4f.Provider.Wewordle,
g4f.Provider.Ylokh,
g4f.Provider.You,
g4f.Provider.Yqcloud,
g4f.Provider.Equing,
g4f.Provider.FastGpt,
g4f.Provider.V50,
g4f.Provider.Wuguokai,
]

text_post = [
'IShowSpeed gets a $1000000 in donation',
'Watch the shop lifter in the Purple!',
'Your package is delayed ',
'shoplifting at its finest',
'Rhino rampaging on a road in India',
'Maybe maybe maybe',
'Run Man Run! Man escapes Police van!',
]

async def run_provider(prompt, index, result_queue):
    try:
        response = await g4f.create_async(
            model="gpt-4",
            
            messages=[{"role": "user", "content": 'Я хочу чтобы ты был в роли переводчика с английского на русский, ты должен переводить предложения не слово в слово, а так как считаешь нужным, плюсом, ты должен переводить на неформальный русский, как будто бы переводишь своему близкому другу, ответь на это сообщение ТОЛЬКО переводом следующего предложения, а также выдели свой перевод (начало и конец) специальным символом @:' + prompt}],
            
        )
        print(response)
    except: 
        print("hueta")

async def main():
    result_queue = asyncio.Queue()
    
    # Create and start tasks
    tasks = [run_provider(text, index, result_queue) for index, text in enumerate(text_post)]
    await asyncio.gather(*tasks)
    

if __name__ == "__main__":
    asyncio.run(main())

# ВАЖНО
# Pillow[14]: Pillow - это библиотека для обработки изображений в Python. Хотя эта библиотека не связана напрямую с DeepL API, она может быть полезна, если вам нужно работать с изображениями вместе с переводом текста. Pillow обеспечивает улучшение и фильтрацию изображений, а также поддерживает множество форматов файлов изображений. Вы можете установить библиотеку с помощью pip:
#    pip install pillow
# Затем вы можете использовать ее для работы с изображениями, например, для изменения размера, обрезки, поворота и других операций.

#    from PIL import Image

#    # Открываем изображение
#    image = Image.open("image.jpg")

#    # Изменяем размер изображения
#    resized_image = image.resize((800, 600))

#    # Сохраняем измененное изображение
#    resized_image.save("resized_image.jpg")
# Этот пример открывает изображение "image.jpg", изменяет его размер до 800x600 пикселей и сохраняет измененное изображение в файл "resized_image.jpg".