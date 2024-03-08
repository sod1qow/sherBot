from loader import dp
from aiogram import types
from database import get_sher
import random


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Salom")


@dp.message_handler(commands=['sher'])
async def sher_command(message: types.Message):
    sherlar = await get_sher()
    result = random.choice(sherlar)
    await message.answer(result[1])

