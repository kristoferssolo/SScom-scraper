"""
Telegram bot for scraper
Author - Kristofers Solo
Licence - MIT
"""
import json
import logging
from pathlib import Path
from aiogram import Bot, Dispatcher, executor, types
from scraper import gpus

BASE_DIR = Path(__file__).resolve().parent

# Read the token from file
with open(Path(BASE_DIR, "config.json"), "r", encoding="UTF-8") as config_file:
    config = json.load(config_file)

API_TOKEN = config["API_TOKEN"]

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@ dp.message_handler(commands=["gpu", "gpus"])
async def gpu_price_message(message: types.Message):
    """Returns all scraped GPUs and their prices to telegram"""
    data = gpus.get_data()
    message_size = 100
    chunked_data = [data[i:i + message_size]
                    for i in range(0, len(data), message_size)]

    for i in chunked_data:
        await message.answer("\n".join(i))
    await message.answer(f"In total {len(data)} GPUs")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
