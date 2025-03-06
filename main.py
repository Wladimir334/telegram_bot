from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import router as client_router

load_dotenv()

# создаём объект бота и диспетчера (маршрутизатора)
bot = Bot(token=getenv("bot_token"))
dp = Dispatcher()
dp.include_router(client_routerweather)



dp.run_polling(bot)





# token = getenv("bot_token")





# Name:  W334_bot
