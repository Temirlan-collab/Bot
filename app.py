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

# Функция для запуска бота
def run_bot():
    print("🚀 Запускаем бота...")
    try:
        asyncio.run(dp.start_polling(bot))
    except Exception as e:
        print(f"❌ Ошибка бота: {e}")

# Функция для проверки, что бот жив (опционально)
@app.route('/status')
def status():
    return "✅ Бот работает"

# Запускаем бота в отдельном потоке при старте Flask
# Даем Flask немного времени, чтобы запуститься, потом стартуем бота
def start_bot_with_delay():
    time.sleep(2)  # Ждем, пока Flask запустится
    run_bot()

if __name__ == "__main__":
    # Запускаем бота в фоновом потоке
    bot_thread = threading.Thread(target=start_bot_with_delay)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Запускаем Flask
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
