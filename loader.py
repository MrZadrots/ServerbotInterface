import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config



loop = asyncio.get_event_loop()
bot = Bot(token='5317656053:AAFTDMFd0ytm46eRWbDxtswCJusr5jW1xZw', parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

