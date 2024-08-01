from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оставить заявку', callback_data='bid' )],
    [InlineKeyboardButton(text='Новости ЖК', callback_data='R_S_news')],
    [InlineKeyboardButton(text='Частые вопросы', callback_data='FAQ')],
    [InlineKeyboardButton(text='Связь с охраной/ресепшен', callback_data='guard_conn')]])

menu_bid = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пропуск КПП/Здание', callback_data='kpp/build')],
    [InlineKeyboardButton(text='Вызов сантехника', callback_data='santteh')],
    [InlineKeyboardButton(text='Вызов электрика', callback_data='electr')],
    [InlineKeyboardButton(text='Другое', callback_data='other')]])

bid_pass = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='КПП(Заявка на ТС)', callback_data='kpp')],
    [InlineKeyboardButton(text='Здание', callback_data='build')]])
