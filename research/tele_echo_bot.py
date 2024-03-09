import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import sys

load_dotenv()
API_TOKEN=os.getenv("TOKEN")
print(API_TOKEN)


logging.basicConfig(level=logging.INFO)

# initialise bot and dispatcher

bot=Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
    #handle /start or */help commands
    
    await message.reply("Welcome to this bot!\nPowered by aiogram.")
    
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)