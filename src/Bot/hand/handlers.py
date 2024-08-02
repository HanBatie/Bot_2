from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from src.Bot.keyboards import kb
from src.Bot.keyboards import inl

from src.db.requests import get_R_C

router = Router()


class kpp_pass_reg(StatesGroup):
    auto_number = State()
    date_time = State()
    full_name = State()


class build_pass_reg(StatesGroup):
    date_time = State()
    annotation = State()
    full_name = State()

@router.message(F.text == 'Всё правильно')
async def main_menu(message: Message):
    await message.answer(f'Здесь представлены мои функции.\n'
                         f'Выберите необходимую функцию:',
                         reply_markup=inl.main_menu)




#@router.message(F.data == 'R_S_news')
#async def main_request_R_S_news(callback: CallbackQuery):
#    await callback.answer('Вы нажали "Новости ЖК"')
#    await callback.message.edit_text()

#@router.message(F.data == 'FAQ')
#async def main_request_FAQ(callback: CallbackQuery):
#    await callback.answer('Вы нажали "Частые вопросы"')
#    await callback.message.edit_text()

#@router.message(F.data == 'guard_conn')
#async def main_request_guard_conn(callback: CallbackQuery):
 #   await callback.answer('Вы нажали "Связь с охраной/ресепшен"')
  #  await callback.message.edit_text()