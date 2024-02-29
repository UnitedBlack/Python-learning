import g4f, asyncio


provs = [
g4f.Provider.ChatBase,
g4f.Provider.Liaobots,
# g4f.Provider.Phind,
]

# if len(prompt + 20) < response:
async def gpt_translate(prompt = "Earn money the old fashion way - inherit it "):
    try: 
        response = await g4f.ChatCompletion.create_async(
        model="gpt-4",
        provider=g4f.Provider.Liaobots,
        messages=[{'role': 'user', 'content': 'Я хочу чтобы ты был в роли переводчика с английского на русский, ты должен переводить предложения не слово в слово, а так как считаешь нужным, плюсом, ты должен переводить на неформальный русский, как будто бы переводишь своему близкому другу, ответь на это сообщение ТОЛЬКО переводом следующего предложения, а также выдели свой перевод (начало и конец) специальным символом @, обязательно перепроверь чтобы твой перевод был внутри специального символа то есть @твой перевод@, так же если мое сообщение содержит эмодзи не используй их в ответе: ' + prompt}],
    )
        print(f"{response}")
    except Exception as e:
        print(f"Not working")
        response = await g4f.ChatCompletion.create_async(
        model="gpt-4",
        provider=g4f.Provider.ChatBase,
        messages=[{'role': 'user', 'content': 'Я хочу чтобы ты был в роли переводчика с английского на русский, ты должен переводить предложения не слово в слово, а так как считаешь нужным, плюсом, ты должен переводить на неформальный русский, как будто бы переводишь своему близкому другу, ответь на это сообщение ТОЛЬКО переводом следующего предложения, а также выдели свой перевод (начало и конец) специальным символом @, обязательно перепроверь чтобы твой перевод был внутри специального символа то есть @твой перевод@, так же если мое сообщение содержит эмодзи не используй их в ответе: ' + prompt}],
        )
        print(f"{response}")
    


asyncio.run(gpt_translate())


# GptChatly x
# Liaobots v
# Myshell x
# Phind v
# GeekGpt vx
