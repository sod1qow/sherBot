from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import logging


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)