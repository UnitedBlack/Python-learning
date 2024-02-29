from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.utils.markdown import hbold, hstrikethrough, hcode, hlink
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from aiogram.types import InputMediaPhoto
from configure_bot import TOKEN, GOO_SO_TOKEN
from datetime import datetime
import sql, tg_sql, ast, logging, json, os, asyncio
from pprint import pprint
from main import initialize
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
headers = {"Content-Type": "application/json"}


class SendPosts(StatesGroup):
    delayed_menu = State()
    delayed_delete = State()
    delayed_change = State()
    start = State()
    sender = State()
    wait_state = State()


def get_third_kb() -> types.ReplyKeyboardMarkup:
    third_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    third_kb.add(
        types.KeyboardButton("Изменить время"),
        types.KeyboardButton("Удалить пост"),
        types.KeyboardButton("Назад"),
    )
    return third_kb


def schedule_post(data):
    result = requests.post(
        url="https://inlinegptbot.unitedblack.repl.co",
        # url="http://127.0.0.1:80",
        data=json.dumps(data),
        headers=headers,
    )

    return result.status_code


def request_delayed_posts():
    data = {"get_delayed_posts": "get_delayed_posts"}
    result = requests.post(
        url="https://inlinegptbot.unitedblack.repl.co",
        # url="http://127.0.0.1:80",
        data=json.dumps(data),
        headers=headers,
    )
    return result.text


def request_delete_delayed(job_id):
    data = {"job_id": job_id}
    result = requests.post(
        url="https://inlinegptbot.unitedblack.repl.co",
        # url="http://127.0.0.1:80",
        data=json.dumps(data),
        headers=headers,
    )
    return result.status_code


def request_change_time(job_id, user_date):
    formatted_date = datetime.strptime(str(user_date), "%d-%m %H:%M")
    data = {
        "job_id": job_id,
        "custom_month": formatted_date.month,
        "custom_day": formatted_date.day,
        "custom_hour": formatted_date.hour,
        "custom_minute": formatted_date.minute,
    }
    result = requests.post(
        url="https://inlinegptbot.unitedblack.repl.co",
        # url="http://127.0.0.1:80",
        data=json.dumps(data),
        headers=headers,
    )
    return result.status_code


def append_data_to_db(wb_id, status):
    post_exist = tg_sql.is_post_in_db(wb_id)
    if post_exist:
        tg_sql.set_post_status(wb_id=wb_id, status=status)
    elif post_exist == False:
        tg_sql.add_post(wb_id=wb_id, status=status)


def get_main_kb() -> types.ReplyKeyboardMarkup:
    main_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_kb.add(
        types.KeyboardButton("Обновить отложку"),
        types.KeyboardButton("Отложка"),
    )
    return main_kb


def get_short_link(link) -> str:
    result = requests.post(
        url="https://goo.su/api/links/create",
        headers={"content-type": "application/json", "x-goo-api-token": GOO_SO_TOKEN},
        data=json.dumps({"url": link}),
    )
    if result.status_code == 200:
        return json.loads(result.text)["link"]["short"]


def wbparse():
    all_products = sql.get_all_products()
    tg_posts: list = tg_sql.get_all_posts()
    filtered_products = [
        product for product in all_products if product["url"] not in tg_posts
    ]
    return filtered_products


def format_post(item):
    name = item.get("name")
    discount_price = item.get("discount_price")
    price = item.get("price")
    star_rating = item.get("star_rating")
    composition = item.get("composition")
    color = item.get("color")
    url = item.get("url")
    try:
        short_url = f"https://goo.su/{get_short_link(url)}"
    except:
        short_url = False

    post = f"🎁 {hbold(name)}" if name else ""
    post += (
        f"\n\n💵Цена: {hstrikethrough(price)}₽ {hbold(discount_price)}₽"
        if price and discount_price
        else ""
    )
    # считать процент скидки
    if float(star_rating) >= 4.8:
        post += (
            f"\n\n⭐️{hbold('Хороший рейтинг')}: {hbold(star_rating)}"
            if star_rating
            else ""
        )
    else:
        post += f"\n\n🌟Рейтинг: {hbold(star_rating)}" if star_rating else ""

    post += f"\n\n🔬Состав: {hbold(composition)}" if composition else ""
    post += f"\n\n🌈Цвет: {hbold(color)}" if color else ""
    post += (
        f"\n\n🔗{hbold('Купить здесь:')} {hlink(url=short_url, title='ссылка на товар')}"
        if short_url
        else url
    )

    return post


def prepare_posts(posts_list):
    # try:
    #     posts_list: list = wbparse()
    # except:
    #     return False

    for item in posts_list:
        posts_list.pop(0)
        url = item.get("url")
        wb_id = item.get("wb_id")
        is_in_db = tg_sql.is_post_in_db(url)
        post_status = tg_sql.get_post_status(url)
        if is_in_db and post_status == "Posted":
            continue
        post, pic_url = format_post(item), item.get("pic_url")
        if len(pic_url) >= 80:
            pic_url = ast.literal_eval(pic_url)

        return post, pic_url, url


@dp.message_handler(regexp="^Обновить отложку$", state="*")
async def add_posts_to_delay(message: types.Message):
    await message.reply(text="Ща обновлю")
    posts_list = wbparse()
    for i in range(1, 21):
        print(i)
        try:
            post_text, pic_url, post_url = prepare_posts(posts_list)
        except TypeError as e:
            await bot.send_message(
                message.chat.id, "Посты закончились или какая-то ошибка"
            )
            await bot.send_message(message.chat.id, e)
            return
        except ValueError:
            post_text, pic_url, post_url = prepare_posts(posts_list)

        delay_data = {"post_text": post_text, "post_pic": pic_url}
        status = schedule_post(delay_data)

        if status != 200:
            await message.reply("Произошла ошибка с отложкой поста")
            continue
        else:
            append_data_to_db(post_url, "Posted")
            continue
    await bot.send_message(message.chat.id, "Сделал")


@dp.message_handler(regexp="^Отложка$", state="*")  # state main menu
async def get_delayed_posts(message: types.Message):
    await SendPosts.delayed_menu.set()
    delayed_post = json.loads(request_delayed_posts())["delayed_posts"]
    if delayed_post:
        delayed_posts = ""
        for delayed in delayed_post:
            jobname = delayed["jobname"]
            jobtime = delayed["jobtime"]
            jobid = delayed["job_id"]
            delayed_posts += f"{jobname}\n{jobtime}\n{hcode(jobid)}\n{'='*32}\n"

        await bot.send_message(
            message.chat.id,
            text=delayed_posts,
            parse_mode="HTML",
            reply_markup=get_third_kb(),
        )
    elif delayed_post == []:
        await bot.send_message(message.chat.id, text="Отложка пустая")


@dp.message_handler(state=SendPosts.delayed_delete)  # state main menu
async def delete_delayed_post(message: types.Message, state: FSMContext):
    delayed_id = message.text
    result = request_delete_delayed(delayed_id)

    if result == 200:
        await message.reply("Удалил")
        await state.finish()
    elif result == 500:
        await message.reply("Произошла какая-то ошибка с удалением")

    await get_delayed_posts(message)


@dp.message_handler(state=SendPosts.delayed_change)
async def change_post_delayed_time(message: types.Message):
    delayed_id = message.text.splitlines()
    request = request_change_time(delayed_id[0], delayed_id[1])
    if request == 200:
        await message.reply("Изменил")
    elif request == 500:
        await message.reply("Произошла какая-то ошибка с изменением")
    await get_delayed_posts(message)


@dp.message_handler(
    regexp="^Удалить пост|Изменить время$", state=SendPosts.delayed_menu
)
async def ask_delayed_id(message: types.Message):
    if message.text == "Удалить пост":
        await SendPosts.delayed_delete.set()
        await bot.send_message(message.chat.id, text="Пришлите ID отложки")

    elif message.text == "Изменить время":
        await SendPosts.delayed_change.set()
        await bot.send_message(
            message.chat.id,
            text="Пришлите ID отложки и время в формате '31(д)-10(м) 10:15'",
        )


@dp.message_handler(commands=["clear"], state="*")
async def clear_tg_db(message: types.Message):
    try:
        tg_sql.close_connection()
        os.remove(tg_sql.db_file)
        await message.reply("БД с тг очищена")
        tg_sql.create_or_connect_database()
    except FileNotFoundError:
        await message.reply("Не могу найти файл")
        return
    except PermissionError:
        print("Закройте все процессы с БД!")
        await message.reply("Закройте все процессы с БД!")


@dp.message_handler(commands=["clear_wb"], state="*")
async def clear_wb_db(message: types.Message):
    try:
        sql.close_connection()
        os.remove(sql.db_file)
        await message.reply("БД с вб очищена")
        sql.create_or_connect_database()
    except FileNotFoundError:
        await message.reply("Не могу найти файл")
        return
    except PermissionError as e:
        print(e)
        print("Закройте все процессы с БД!")
        await message.reply("Закройте все процессы с БД!")


@dp.message_handler(commands=["parse"], state="*")
async def call_parser(message: types.Message):
    await bot.send_message(message.chat.id, text="Вызываю, подождите пару минут")
    # send gif
    await initialize()
    await bot.send_message(message.chat.id, text="Сделано")


@dp.message_handler(regexp="^Назад$", state="*")
async def main_menu(message: types.Message):
    # await SendPosts.start.set()
    await bot.send_message(
        message.chat.id, text="Вы в главном меню", reply_markup=get_main_kb()
    )


@dp.message_handler(commands=["start"], state="*")
async def start_point(message: types.Message):
    await main_menu(message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
