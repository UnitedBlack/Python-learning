from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, text=config.greeting_message, parse_mode="HTML", disable_web_page_preview=True)
    
    
if __name__ == "__main__":
    executor.start_polling(dp)
