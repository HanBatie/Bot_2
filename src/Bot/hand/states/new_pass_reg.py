from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router

from src.Bot.keyboards import inl
import src.db.requests as rq

router_pass = Router()


class kpp_pass_reg(StatesGroup):
    tg_id = State()
    auto_number = State()
    date_time = State()
    full_name = State()


class build_pass_reg(StatesGroup):
    tg_id = State()
    date_time = State()
    annotation = State()
    full_name = State()


@router_pass.message(F.text == 'Всё правильно')
async def main_menu(message: Message):
    await message.answer(f'Здесь представлены мои функции.\n'
                         f'Выберите необходимую:', reply_markup=inl.main_menu)


@router_pass.callback_query(F.data == 'bid')
async def main_request_bid(callback: CallbackQuery):
    await callback.answer('Вы нажали "Оставить заявку"')
    await callback.message.answer("Выберите категорию заявки", reply_markup=inl.menu_bid)


@router_pass.callback_query(F.data == 'kpp/build')
async def new_pas(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('dsa')


@router_pass.callback_query(F.data == 'kpp')
async def get_auto_number(callback: CallbackQuery, state: FSMContext):
    await state.set_state(kpp_pass_reg.auto_number)
    await callback.answer('Вы нажали "КПП(Заявка на ТС)"')
    await callback.message.answer('Введите номер ТС. Пример: С123ВА77')


@router_pass.message(kpp_pass_reg.auto_number)
async def get_kpp_date_time(message: Message, state: FSMContext):
    await state.update_data(auto_number=message.text)
    await state.set_state(kpp_pass_reg.date_time)
    await message.answer('Введите дату и время проезда ТС. Пример: 23.11 14:00-18:00')


@router_pass.message(kpp_pass_reg.date_time)
async def get_kpp_full_name(message: Message, state: FSMContext):
    await state.update_data(data_time=message.text)
    await state.set_state(kpp_pass_reg.full_name)
    await message.answer('Для завершения регистрации введите Ваше ФИО:')


@router_pass.message(kpp_pass_reg.full_name)
async def end_kpp_reg(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer("Заявка успешно создана")


@router_pass.callback_query(F.data == 'build')
async def get_auto_number(callback: CallbackQuery, state: FSMContext):
    await state.set_state(build_pass_reg.date_time)
    await callback.answer('Вы нажали "Здание"')
    await callback.message.answer('Введите дату и время проезда ТС. Пример: 23.11 14:00-18:00')


@router_pass.message(build_pass_reg.date_time)
async def get_build_date_time(message: Message, state: FSMContext):
    await state.update_data(date_time=message.text)
    await state.set_state(build_pass_reg.annotation)
    await message.answer('Введите коментарий или "-"')


@router_pass.message(build_pass_reg.date_time)
async def get_build_full_name(message: Message, state: FSMContext):
    await state.update_data(annotation=message.text)
    await state.set_state(build_pass_reg.full_name)
    await message.answer('Для завершения регистрации введите Ваше ФИО:')


@router_pass.message(build_pass_reg.full_name)
async def end_build_reg(message: Message, state: FSMContext):
    await state.update_data(tg_id = message.from_user.id)
    await state.update_data(full_name=message.text)
    data = await state.get_data()
    await rq.db_add_kpp_pass(data['tg_id'], data['auto_number'], data['date_time'], data['full_name'])
    await message.answer("Заявка успешно создана")
    await state.clear()
