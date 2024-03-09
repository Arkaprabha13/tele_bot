from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import openai
import sys



class Reference:
    '''
    This class is used to store the reference to the bot and the dispatcher
    '''
    
    def __init__(self) -> None:
        self.response=""




load_dotenv()
TOKEN=os.getenv("TOKEN")
openai.api_key=os.getenv("OPEN_API_KEY")

reference= Reference()

model_name="gpt-3.5-turbo"


bot= Bot(token=TOKEN)
dispatcher=  Dispatcher(bot)


def clear_past_response():
    '''
    This function is used to clear the past response of the bot
    '''
    reference.response=""
    


@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    
    #handle /start or */help commands
    
    await message.reply("Welcome to this bot!\nPowered by aiogram.")
    
    
@dispatcher.message_handler(commands=['clear'])
async def welcome(message: types.Message):
    
    #handle /start or */help commands
    clear_past_response()
    await message.reply("The past response has been cleared.")
     
@dispatcher.message_handler(commands=['help'])
async def welcome(message: types.Message):
    
    await message.reply("This bot is powered by OpenAI's GPT-3.5 model. You can ask any question and the bot will try to answer it.\n /start: Start the bot\n /help: Get help\n /clear: Clear the past response")

@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    '''
    This function is used to chat with the GPT-3.5 model
    '''
    print(f" >>> User: \t {message.text}")
    
    try:
        response= openai.ChatCompletion.create(
            model=model_name,
            messages=[{"role":"assistant","content":reference.response},{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": message.text}],
            # prompt=message.text,
            # temperature=0.7,
            max_tokens=20
        )
        
        reference.response=response.choices[0].text
        print(f"\n <<< Bot: \t\n {reference.response}")
        await bot.send_message(chat_id=message.chat.id, text=reference.response)
        
    except Exception as e:
        print(e)
        await message.answer("Sorry, I am not able to answer that.")
    
   

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
    
    