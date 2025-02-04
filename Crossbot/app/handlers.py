from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb
import app.database.requests as rq

router = Router()
photo = "AgACAgIAAxkBAAOIZvlMFm0Xd8jF36grKnma7KQe2vAAAs7eMRs78MlL8P4SWl9OhvgBAAMCAAN5AAM2BA"
start_caption = "Привет! 👟 Добро пожаловать\nв магазин кроссовок!\nЗдесь вы найдете последние модели,\nи лучшие бренды.\nЧтобы начать, выберите один из вариантов:"
last_brend = ""

@router.message(CommandStart())
async def cmd_start(message: Message):
    # Обрабатывает команду /start и сохраняет пользователя
    await rq.set_user(message.from_user.id)
    await message.answer_photo(photo=photo, caption=start_caption, reply_markup=kb.main)

@router.callback_query(F.data == "back_1")
async def cmd_start(callback: CallbackQuery):
    # Возвращает к приветственному сообщению
    await callback.message.edit_caption(caption=start_caption, reply_markup=kb.main)

@router.callback_query(F.data == 'catolog')
async def catalog(callback: CallbackQuery):
    # Запрашивает выбор бренда для показа кроссовок
    await callback.message.edit_caption(caption='Выберите бренд', reply_markup=await kb.categories())

@router.callback_query(F.data == "back_2")
async def catalog(callback: CallbackQuery):
    # Повторно показывает выбор категории брендов
    await callback.message.edit_caption(caption='Выберите бренд', reply_markup=await kb.categories())

@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    # Обрабатывает выбор категории и запрашивает товары этой категории
    global last_brend
    last_brend = callback.data.split('_')[1]
    await callback.message.edit_caption(caption='Выберите товар', reply_markup=await kb.items(last_brend))

@router.callback_query(F.data == 'back_3')
async def category(callback: CallbackQuery):
    # Возвращает к выбору товаров данной категории
    await callback.message.edit_caption(caption='Выберите товар', reply_markup=await kb.items(last_brend))

@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    # Показывает информацию о выбранном товаре
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.message.edit_caption(caption=f'Название: {item_data.name}\nЦена: {item_data.price}₽\nОписание: {item_data.description}', reply_markup=kb.back_3)

@router.callback_query(F.data == 'description')
async def description(callback: CallbackQuery):
    # Предоставляет информацию о возможностях бота
    await callback.message.edit_caption(caption='👟 Добро пожаловать в бот магазина кроссовок!\nНаш бот создан специально для вас, чтобы упростить процесс выбора и покупки кроссовок.\nВозможности бота:\n- 🌟 Просмотр ассортимента: Узнайте о новых поступлениях и популярных моделях.\n- 🛒 Получение информации: Узнавайте цены, размеры и наличие.\n- 🎯 Простая навигация: Легко находите нужные товары по категориям.\nПока мы добавляем новые функции, просто задавайте вопросы о товарах, и я помогу вам с выбором! Присоединяйтесь к нашему обувному сообществу! Найдите идеальные кроссовки и будьте всегда в тренде!', reply_markup=kb.description_kb) 

@router.callback_query(F.data == 'contact')
async def contact(callback: CallbackQuery):
    # Предоставляет контактную информацию для связи
    await callback.message.edit_caption(caption="Контакты\n \n📞 Связь с нами, сотрудничество:\n @DeKuNe_tyan", reply_markup=kb.contact_kb)

