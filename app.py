# app.py
import os
import asyncio
import threading
from flask import Flask
from bot import dp, bot  # Импортируем вашего бота

app = Flask(__name__)

@app.route('/')
def home():
    return "Бот NEO.LAB запущен!"

@app.route('/health')
def health():
    return "OK"

# Функция для запуска бота в фоновом потоке
def run_bot():
    asyncio.run(dp.start_polling(bot))

# Запускаем бота при старте веб-сервера
threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)