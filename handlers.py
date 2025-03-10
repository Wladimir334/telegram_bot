from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

from weather_api import get_weather

router = Router()

@router.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("Привет. Спроси у меня что-нибудь.")

@router.message(Command(commands=["help"]))
async def process_start_command(message: Message):
    await message.answer("Привет. Выбери нужное действие.")

@router.message(Command(commands=["weather"]))
async def process_start_command(message: Message):
    weather = get_weather()
    await message.answer("Погода на сегодня: ")

@router.message(Command(commands=["vacancies"]))
async def process_start_command(message: Message):
    await message.answer("Есть вакансий: ")

@router.message(Command(commands=["courses"]))
async def process_start_command(message: Message):
    await message.answer("Курс доллара на сегодня: ")

