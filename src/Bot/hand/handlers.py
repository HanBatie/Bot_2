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

@router.message(F.text == 'Всё правильно')
async def main_menu(message: Message):
    await message.answer(f'Здесь представлены мои функции.\n'
                         f'Выберите необходимую:', reply_markup=inl.main_menu)


@router.callback_query(F.data == 'bid')
async def main_request_bid(callback: CallbackQuery):
    await callback.answer('Вы нажали "Оставить заявку"')
    await callback.message.answer("Выберите категорию заявки", reply_markup=inl.menu_bid)


@router.callback_query(F.data == 'kpp/build')
async def new_pas(callback: CallbackQuery):
    await callback.answer('Вы нажали "Пропуск КПП/Здание"')
    await callback.message.edit_text('Выберите тип', reply_markup=inl.bid_pass)


@router.callback_query(F.data == 'kpp')
async def get_auto_number(callback: CallbackQuery, state: FSMContext):
    await state.set_state(kpp_pass_reg.auto_number)
    await callback.answer('Вы нажали "КПП(Заявка на ТС)"')
    await callback.message.answer('Введите номер ТС. Пример: С123ВА77')


@router.message(kpp_pass_reg.auto_number)
async def get_kpp_date_time(message: Message, state: FSMContext):
    await state.update_data(auto_number=message.text)
    await state.set_state(kpp_pass_reg.date_time)
    await message.answer('Введите дату и время проезда ТС. Пример: 23.11 14:00-18:00')


@router.message(kpp_pass_reg.date_time)
async def get_kpp_full_name(message: Message, state: FSMContext):
    await state.update_data(data_time=message.text)
    await state.set_state(kpp_pass_reg.full_name)
    await message.answer('Для завершения регистрации введите Ваше ФИО:')


@router.message(kpp_pass_reg.full_name)
async def end_kpp_reg(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer("Заявка успешно создана")


@router.callback_query(F.data == 'build')
async def get_auto_number(callback: CallbackQuery, state: FSMContext):
    await state.set_state(build_pass_reg.date_time)
    await callback.answer('Вы нажали "Здание"')
    await callback.message.answer('Введите дату и время проезда ТС. Пример: 23.11 14:00-18:00')


@router.message(build_pass_reg.date_time)
async def get_build_date_time(message: Message, state: FSMContext):
    await state.update_data(date_time=message.text)
    await state.set_state(build_pass_reg.annotation)
    await message.answer('Введите коментарий или "-"')


@router.message(build_pass_reg.date_time)
async def get_build_full_name(message: Message, state: FSMContext):
    await state.update_data(annotation=message.text)
    await state.set_state(build_pass_reg.full_name)
    await message.answer('Для завершения регистрации введите Ваше ФИО:')


@router.message(build_pass_reg.full_name)
async def end_build_reg(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer("Заявка успешно создана")


@router.callback_query(F.data == 'santteh')
async def new_santteh(callback: CallbackQuery):
        await callback.answer('Вы нажали "Вызов сантехника"')
        await callback.message.edit_text("Сервис в разработке")



@router.callback_query(F.data == 'electr')
async def new_electric(callback: CallbackQuery):
        await callback.answer('Вы нажали "Вызов электрика"')
        await callback.message.edit_text("Сервис в разработке")



@router.callback_query(F.data == 'other')
async def other_inf(callback: CallbackQuery):
        await callback.answer('Вы нажали "Другое"')
        await callback.message.edit_text("Сервис в разработке")





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