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

# Функция для запуска бота (запускается в главном потоке)
def run_bot():
    print("🚀 Запускаем бота...")
    try:
        # Создаём новый event loop в главном потоке
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(dp.start_polling(bot))
    except Exception as e:
        print(f"❌ Ошибка бота: {e}")

# ЗАПУСКАЕМ БОТА В ГЛАВНОМ ПОТОКЕ
print("⏳ Инициализация бота...")

# Создаём и запускаем event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

print("🚀 Запускаем бота...")
try:
    # Запускаем бота в текущем потоке (главном)
    loop.run_until_complete(dp.start_polling(bot))
except Exception as e:
    print(f"❌ Ошибка бота: {e}")
