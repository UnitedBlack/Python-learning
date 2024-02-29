import g4f, asyncio


async def gpt_translate(prompt):
    response = await g4f.ChatCompletion.create_async(
        model="gpt-4",
        provider=g4f.Provider.FreeGpt,
        messages=[{'role': 'user', 'content': 'Я хочу чтобы ты был в роли переводчика с английского на русский, ты должен переводить предложения не слово в слово, а так как считаешь нужным, плюсом, ты должен переводить на неформальный русский, как будто бы переводишь своему близкому другу, ответь на это сообщение ТОЛЬКО переводом следующего предложения, а также выдели свой перевод (начало и конец) специальным символом @: ' + prompt}],
    )
    return response