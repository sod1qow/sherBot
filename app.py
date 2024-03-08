from aiogram import executor
from loader import dp, Dispatcher
from database import create_tables


async def on_startup(dp):
    await create_tables()
    import user_handlers



if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)

