import os

from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

from app.send_album import send_album

from app.database.requests import set_user
from app.database.requests import get_users

from logger import logger


ADMIN = int(os.getenv("ADMIN"))

class Input(StatesGroup):
    query = State()
    value = State()

class AwaitInput(StatesGroup):
    await_input = State()

router = Router()


# Обработчик команды /start
@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    if await state.get_state() == AwaitInput.await_input: return
    await state.clear()
    await message.answer(
    "👋 Привет! Я — бот, который найдет тебе фотографии по твоему запросу.\n"
    "Нажми на кнопку *Поиск фото*, чтобы начать 🔎",
    reply_markup=kb.search_photo
)

    await set_user(message)


@router.message(Command("user_info"))
async def start_handler(message: Message):
    if message.from_user.id != ADMIN: return
    all_users = await get_users()
    if not all_users: return await message.answer("No users")

    await message.answer(f"USERS:")

    for user in all_users:
        text = (f"ID: {user.id}\
        \nTG_ID: {user.tg_id}\
        \nusername: {user.username}\
        \nfull_name: {user.full_name}\
        \ndata registration: {user.data}")
        await message.answer(text)

@router.message(F.text == "Поиск фото")
async def reg_one(message: Message, state: FSMContext):
    if await state.get_state() == AwaitInput.await_input:
        data = await state.get_data()
        await message.answer(f"ожидайте пока идет поиск: \n{data["query"]} \n{data["value"]}")
    else:
        await state.set_state(Input.query)
        await message.answer("Введите запрос", reply_markup=ReplyKeyboardRemove())


@router.message(Input.query)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(query=message.text)
    await state.set_state(Input.value)
    await message.answer("Введите количество", reply_markup=kb.value)


@router.message(Input.value)
async def reg_three(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(value=message.text)
        data = await state.get_data()
        query = data["query"]
        value = data["value"]
        value = min(int(value), 99)
        await state.set_state(AwaitInput.await_input)
        await message.answer(f"ожидайте пока идет поиск: \n{query} \n{value}")
        try:
            await send_album(message, query, int(value))
        except Exception as e:
            logger.warning(f"Не удалось найти фото // {e}")
            await message.answer(f"Не удалось найти фото")
        await state.clear()
        await message.answer("Хотите найти еще фото, используйте кнопку: (поиск фото), reply_markup=kb.search_photo)

    else: await message.answer("Введите цифры")





