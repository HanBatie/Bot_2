from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import F, Router
from aiogram.filters import CommandStart, CommandObject

from src.Bot.keyboards import kb
import src.db.requests as rq

class user_reg(StatesGroup):
    R_C_id = State()
    phone_number = State()
    name = State()
    Building_adress = State()


router_reg = Router()

#@router_reg.message(CommandStart())
#async def start(message: Message, state: FSMContext):
 #   await message.answer('Здравствуйте, введите ключ подключения:')
  #  await  state.set_state(user_reg.R_C_id)

#@router_reg.message(user_reg.R_C_id)
#async def get_R_C_id(message: Message, state: FSMContext):
#    db_R_C = await rq.get_R_C(message.text)
#    await state.update_data(R_C_id = db_R_C[1])
#    await message.answer(f'Здравствуйте, вы перешли в бота {db_R_C[0]}.'
#                             f'\nДля последующего использования вам необходимо зарегестрироваться',
#                             reply_markup=kb.start_reg)

@router_reg.message(CommandStart(deep_link=True))
async def get_key(message: Message, command: CommandObject, state: FSMContext):
    if command.args is None:
        await message.answer('Здравствуйте, введите ключ подключения:')
    else:
        db_R_C = await rq.get_R_C(command.args)
        await state.update_data(R_C_id = db_R_C[1])
        await message.answer(f'Здравствуйте, вы перешли в бота {db_R_C[0]}.'
                             f'\nДля последующего использования вам необходимо зарегестрироваться',
                             reply_markup=kb.start_reg)


@router_reg.message(lambda message: message.text in ['Начать регистрацию', 'Зарегестрироваться заново'])
async def reg(message: Message, state: FSMContext):
    await message.answer(f'Здравствуйте, для использования вам необходимо зарегистрироваться\n'
                         f'Введите Ваше имя:')
    await state.set_state(user_reg.name)


@router_reg.message(user_reg.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(user_reg.phone_number)
    await message.answer('Отправить телефон', reply_markup=kb.get_number)


@router_reg.message(user_reg.phone_number)
async def get_number(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    await state.set_state(user_reg.Building_adress)
    await message.answer(f'Введите адресс вашего дома\n'
                         f'Достаточно только числа) Пример: улица Ломоносова 32 к. 4 => 324')


@router_reg.message(user_reg.Building_adress)
async def get_adress(message: Message, state: FSMContext):
        await state.update_data(Building_adress=message.text)
        data = await state.get_data()
        await message.answer(f'Регистрация завершена, проверьте корректность введённых данных:'
                                    f'\n Ваше имя: {data["name"]}'
                                    f'\n Номер телефона: {data["phone_number"]}'
                                    f'\n Адресс: {data["Building_adress"]}',
                             reply_markup= kb.end_reg
                            )
        await rq.db_add_user(int(message.from_user.id), data["phone_number"], data["name"], data["Building_adress"], data['R_C_id'])
        await state.clear()