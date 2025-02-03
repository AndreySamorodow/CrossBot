from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_category_item


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Католог", callback_data="catolog")],
    [InlineKeyboardButton(text="Описание", callback_data="description"), InlineKeyboardButton(text="Контакты", callback_data="contact")]
])

async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='back_1'))
    return keyboard.adjust(2).as_markup()

async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='back_2'))
    return keyboard.adjust(2).as_markup()

back_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='back_3')]
])

description_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Католог', callback_data='catolog')],
    [InlineKeyboardButton(text='Контакты', callback_data='contact')]
])

contact_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Католог', callback_data='catolog')],
    [InlineKeyboardButton(text='Описание', callback_data='description')]
])