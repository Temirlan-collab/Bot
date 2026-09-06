import os
import asyncio
import threading
import time
from flask import Flask
from bot import dp, bot

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Бот NEO.LAB запущен! Статус: OK"

@app.route('/health')
def health():
    return "OK"

@app.route('/status')
def status():
    return "✅ Бот работает"

# Функция для запуска бота
def run_bot():
    print("🚀 Запускаем бота...")
    try:
        asyncio.run(dp.start_polling(bot))
    except Exception as e:
        print(f"❌ Ошибка бота: {e}")

# ЗАПУСКАЕМ БОТА СРАЗУ ПРИ ИМПОРТЕ
print("⏳ Инициализация бота...")
bot_thread = threading.Thread(target=run_bot, daemon=True)
bot_thread.start()
print("✅ Бот запущен в фоновом потоке!")
