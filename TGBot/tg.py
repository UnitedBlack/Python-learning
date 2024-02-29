# import t3nsor
import os
import hashlib
# import t3nsor
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
from background import keep_alive
from datetime import datetime

bot = Bot(token='6471699804:AAGGn86o0zTLOUdB1xDDlsPJoz7XbNwKOfE')
dp = Dispatcher(bot)

DESCRIPTION = 'Я Inline бот, который использует ChatGPT для ответа на твои запросы, это значит что я могу отвечать тебе \
      из любого чата (даже из "избранные"), для понимания как мной правильно пользоваться напиши /help.'

HELP = '1. Пишешь запрос в любом чате. 2. После этого добавляешь в начало строки моё имя (@findgpt3bot) 3. Ждёшь загрузки, после нажимаешь на кнопку "Ответ готов, нажми сюда"'


def chat_gpt(prompt_user):
    messages = []
    t3nsor_cmpl = t3nsor.Completion.create(
        prompt=prompt_user,
        messages=messages)
    result = asyncio.run(get_gpt_response())
    print('gpt:', t3nsor_cmpl.completion.choices[0].text)
    messages.extend([
        {'role': 'user', 'content': prompt_user},
        {'role': 'assistant',
            'content': t3nsor_cmpl.completion.choices[0].text}])
    return t3nsor_cmpl.completion.choices[0].text


@dp.message_handler(commands=['start', 'help'])
async def message_handler(message: types.Message):
    user = message.from_user
    user_option = message.text
    if user_option == "/start":
        await message.reply(f"Привет, {user.username}. {DESCRIPTION}")
    elif user_option == "/help":
        await message.reply(HELP)
        with open("imgs/FirstStep.png", "rb") as first_step, open("imgs/SecondStep.png", "rb") as second_step, \
                open("imgs/ThirdStep.png", "rb") as third_step:
            first_step_input = types.InputFile(first_step)
            second_step_input = types.InputFile(second_step)
            third_step_input = types.InputFile(third_step)
            await message.answer_media_group(
                media=[types.InputMediaPhoto(media=first_step_input), types.InputMediaPhoto(media=second_step_input),
                       types.InputMediaPhoto(media=third_step_input)])


@dp.message_handler()
async def message_handler(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    await message.reply(chat_gpt(message.text))


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery,):
    text = query.query or "echo"
    user = query.from_user
    result = await chat_gpt(query.query)
    result_id = hashlib.md5(
        (text + str(datetime.now().timestamp())).encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title="Ответ готов, нажми сюда",
        input_message_content=types.InputTextMessageContent(
            message_text=f"{user.username}: {text}\nGPT-3.5: {result}"))]

    await query.answer(articles, cache_time=60, is_personal=True)

keep_alive()
executor.start_polling(dp, skip_updates=True)


bot = Bot(token='6471699804:AAGGn86o0zTLOUdB1xDDlsPJoz7XbNwKOfE')
dp = Dispatcher(bot)

DESCRIPTION = 'Я Inline бот, который использует ChatGPT для ответа на твои запросы, это значит что я могу отвечать тебе \
      из любого чата (даже из "избранные"), для понимания как мной правильно пользоваться напиши /help.'

HELP = '1. Пишешь запрос в любом чате. 2. После этого добавляешь в начало строки моё имя (@findgpt3bot) 3. Ждёшь загрузки, после нажимаешь на кнопку "Ответ готов, нажми сюда"'


async def chat_gpt_async(prompt_user):
    messages = []
    t3nsor_cmpl = t3nsor.Completion.create(
        prompt=prompt_user,
        messages=messages)
    print('gpt:', t3nsor_cmpl.completion.choices[0].text)
    messages.extend([
        {'role': 'user', 'content': prompt_user},
        {'role': 'assistant',
            'content': t3nsor_cmpl.completion.choices[0].text}])
    return t3nsor_cmpl.completion.choices[0].text


def chat_gpt(prompt_user):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(chat_gpt_async(prompt_user))


@dp.message_handler(commands=['start', 'help'])
async def message_handler(message: types.Message):
    user = message.from_user
    user_option = message.text
    if user_option == "/start":
        await message.reply(f"Привет, {user.username}. {DESCRIPTION}")
    elif user_option == "/help":
        await message.reply(HELP)
        with open("imgs/FirstStep.png", "rb") as first_step, open("imgs/SecondStep.png", "rb") as second_step, open("imgs/ThirdStep.png", "rb") as third_step:
            first_step_input = types.InputFile(first_step)
            second_step_input = types.InputFile(second_step)
            third_step_input = types.InputFile(third_step)
            await message.answer_media_group(
                media=[types.InputMediaPhoto(media=first_step_input), types.InputMediaPhoto(media=second_step_input),
                       types.InputMediaPhoto(media=third_step_input)])


@dp.message_handler()
async def message_handler(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    await message.reply(await chat_gpt_async(message.text))


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery,):
    text = query.query or "echo"
    user = query.from_user
    result = await chat_gpt_async(query.query)
    result_id = hashlib.md5(
        (text + str(datetime.now().timestamp())).encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title="Ответ готов, нажми сюда",
        input_message_content=types.InputTextMessageContent(
            message_text=f"{user.username}: {text}\nGPT-3.5: {result}"))]

    await query.answer(articles, cache_time=120, is_personal=True)


keep_alive()
executor.start_polling(dp, skip_updates=True)
