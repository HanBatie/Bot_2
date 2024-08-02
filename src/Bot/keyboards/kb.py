from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
                                                           request_contact=True)]],
                                 resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Нажмите кнопку для быстрой отправки')

start_reg = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Начать регистрацию')],
                                          [KeyboardButton(text='Не тот ЖК')]],
                                 resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите пункт меню...')

end_reg = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Всё правильно')],
                                        [KeyboardButton(text='Зарегестрироваться заново')]],
                                resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Проверьте всё тщательно')
