import os
import asyncio
from flask import Flask
from bot import dp, bot

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Бот NEO.LAB работает!"

@app.route('/health')
def health():
    return "OK"

@app.route('/status')
def status():
    return "✅ Бот работает"

# Запускаем бота в главном потоке
print("🚀 Запускаем бота...")

# Создаём event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

try:
    # Запускаем бота
    loop.run_until_complete(dp.start_polling(bot))
except Exception as e:
    print(f"❌ Ошибка бота: {e}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
