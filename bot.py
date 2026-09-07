import json
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import KeyboardButton, WebAppInfo, ReplyKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

if not BOT_TOKEN or not ADMIN_ID:
    print("❌ Ошибка: не найдены BOT_TOKEN или ADMIN_ID в .env файле")
    exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ===== КЛАВИАТУРЫ =====

def main_keyboard():
    kb = [
        [types.KeyboardButton(text="📋 Услуги и цены")],
        [types.KeyboardButton(text="💰 Тарифы"), types.KeyboardButton(text="❓ Частые вопросы")],
        [types.KeyboardButton(text="🖼️ Портфолио"), types.KeyboardButton(text="📞 Контакты")],
        [types.KeyboardButton(text="📩 Отправить заявку"), types.KeyboardButton(text="🚀 Web App")],
        [types.KeyboardButton(text="🆘 Помощь")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def web_app_keyboard():
    button = KeyboardButton(
        text="🚀 Открыть калькулятор услуг",
        web_app=WebAppInfo(url="https://fullcuclelab.netlify.app/tg-app.html")
    )
    return ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)

# ===== КОМАНДЫ =====

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Я — бот студии NEO.LAB.\n"
        "Выберите нужный раздел в меню ниже:",
        reply_markup=main_keyboard()
    )

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "🆘 Помощь\n\n"
        "Доступные команды:\n"
        "/start - Главное меню\n"
        "/services - Услуги и цены\n"
        "/price - Рассчитать стоимость\n"
        "/tariffs - Подробные тарифы\n"
        "/portfolio - Портфолио\n"
        "/order - Оставить заявку\n"
        "/faq - Частые вопросы\n"
        "/contacts - Контакты\n"
        "/support - Техподдержка\n"
        "/id - Мой ID",
        reply_markup=main_keyboard()
    )

@dp.message(Command("services"))
async def services_command(message: types.Message):
    await message.answer(
        "📋 Услуги NEO.LAB\n\n"
        "🛰 Сайты - от 150 000 ₸\n"
        "🤖 Боты - от 50 000 ₸\n"
        "🌐 Переводы - от 2 500 ₸/стр.\n\n"
        "Подробнее: /tariffs",
        reply_markup=main_keyboard()
    )

@dp.message(Command("price"))
async def price_command(message: types.Message):
    await message.answer(
        "💰 Расчет стоимости\n\n"
        "• Лендинг: от 150 000 ₸\n"
        "• Сайт + бот: от 350 000 ₸\n"
        "• Комплекс: от 600 000 ₸\n\n"
        "Для точного расчета отправьте /order",
        reply_markup=main_keyboard()
    )

@dp.message(Command("tariffs"))
async def tariffs_command(message: types.Message):
    await message.answer(
        "📊 Тарифы\n\n"
        "🚀 СТАРТ - 150 000 ₸ (3-5 дней)\n"
        "   • До 5 экранов\n"
        "   • Адаптив\n"
        "   • Форма заявки\n\n"
        "🔥 БИЗНЕС - 350 000 ₸ (10-14 дней)\n"
        "   • Многостраничный сайт\n"
        "   • Telegram-бот\n"
        "   • 60 дней поддержки\n\n"
        "💎 ГЛОБАЛ - от 600 000 ₸ (3-5 недель)\n"
        "   • Всё из Бизнес\n"
        "   • Двуязычная версия\n"
        "   • Приоритетная поддержка",
        reply_markup=main_keyboard()
    )

@dp.message(Command("portfolio"))
async def portfolio_command(message: types.Message):
    await message.answer(
        "🖼️ Портфолио\n\n"
        "🔹 NOVA Store - интернет-магазин\n"
        "🔹 Fresh24 - бот доставки\n"
        "🔹 SaaS локализация\n\n"
        "Сайт: https://fullcuclelab.netlify.app",
        reply_markup=main_keyboard()
    )

@dp.message(Command("order"))
async def order_command(message: types.Message):
    await message.answer(
        "📩 Заявка\n\n"
        "Напишите в одном сообщении:\n"
        "1. Ваше имя\n"
        "2. Услуга\n"
        "3. Описание\n"
        "4. Телефон\n\n"
        "Пример:\n"
        "Иван Петров\n"
        "Нужен сайт\n"
        "+7 777 123-45-67",
        reply_markup=main_keyboard()
    )

@dp.message(Command("faq"))
async def faq_command(message: types.Message):
    await message.answer(
        "❓ Частые вопросы\n\n"
        "1. Цена от сложности\n"
        "2. Дизайн на ваш выбор\n"
        "3. Оплата 50/50\n"
        "4. Гарантия 30 дней\n"
        "5. Сроки: от 3 дней",
        reply_markup=main_keyboard()
    )

@dp.message(Command("contacts"))
async def contacts_command(message: types.Message):
    await message.answer(
        "📞 Контакты NEO.LAB\n\n"
        "📱 Телефон: +7 (777) 206-24-88\n"
        "✈️ Telegram: @FullCycle_bot\n"
        "📧 Email: hello@neolab.studio\n"
        "🌐 Сайт: https://fullcuclelab.netlify.app\n\n"
        "🕒 Режим работы: Пн-Вс, 10:00-22:00 (AST)",
        reply_markup=main_keyboard()
    )

@dp.message(Command("support"))
async def support_command(message: types.Message):
    await message.answer(
        "🛟 Техническая поддержка\n\n"
        "📱 +7 (777) 206-24-88\n"
        "✈️ @FullCycle_bot\n\n"
        "⏱️ Отвечаю в течение 15 минут!",
        reply_markup=main_keyboard()
    )

@dp.message(Command("id"))
async def get_id(message: types.Message):
    await message.answer(
        f"🆔 Ваш ID: {message.from_user.id}\n\n"
        f"Имя: {message.from_user.first_name}\n"
        f"Username: @{message.from_user.username or 'нет'}\n\n"
        f"ADMIN_ID={message.from_user.id}",
        reply_markup=main_keyboard()
    )

# ===== КНОПКИ =====

@dp.message(lambda message: message.text == "📋 Услуги и цены")
async def btn_services(message: types.Message):
    await services_command(message)

@dp.message(lambda message: message.text == "💰 Тарифы")
async def btn_tariffs(message: types.Message):
    await tariffs_command(message)

@dp.message(lambda message: message.text == "❓ Частые вопросы")
async def btn_faq(message: types.Message):
    await faq_command(message)

@dp.message(lambda message: message.text == "🖼️ Портфолио")
async def btn_portfolio(message: types.Message):
    await portfolio_command(message)

@dp.message(lambda message: message.text == "📞 Контакты")
async def btn_contacts(message: types.Message):
    await contacts_command(message)

@dp.message(lambda message: message.text == "📩 Отправить заявку")
async def btn_order(message: types.Message):
    await order_command(message)

@dp.message(lambda message: message.text == "🚀 Web App")
async def btn_webapp(message: types.Message):
    await message.answer("🚀 Откройте форму:", reply_markup=web_app_keyboard())

@dp.message(lambda message: message.text == "🆘 Помощь")
async def btn_help(message: types.Message):
    await help_command(message)

# ===== ПЕРЕСЫЛКА СООБЩЕНИЙ АДМИНУ =====

@dp.message()
async def forward_to_admin(message: types.Message):
    """Пересылает все сообщения от пользователей админу"""
    
    if str(message.from_user.id) == ADMIN_ID:
        return
    
    if message.text and message.text.startswith('/'):
        return
    
    if message.web_app_data:
        return
    
    try:
        await bot.send_message(
            chat_id=ADMIN_ID,
            text=f"📩 Сообщение от @{message.from_user.username or 'нет'} (ID: {message.from_user.id}):\n\n{message.text}"
        )
        await message.answer(
            "✅ Ваше сообщение отправлено! Я отвечу в ближайшее время."
        )
    except Exception as e:
        print(f"Ошибка пересылки: {e}")

# ===== WEB APP =====

@dp.message(lambda message: message.web_app_data is not None)
async def handle_web_app_data(message: types.Message):
    try:
        data = json.loads(message.web_app_data.data)
        notification = (
            "📩 НОВАЯ ЗАЯВКА из Web App!\n\n"
            f"Имя: {data.get('name', 'Не указано')}\n"
            f"Телефон: {data.get('phone', 'Не указан')}\n"
            f"Услуга: {data.get('service', 'Не выбрана')}\n"
            f"Описание: {data.get('description', 'Нет описания')}"
        )
        await bot.send_message(chat_id=ADMIN_ID, text=notification)
        await message.answer("✅ Спасибо! Заявка принята.", reply_markup=main_keyboard())
    except Exception as e:
        print(f"Ошибка Web App: {e}")
