import asyncio
import logging
import openai

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types 
from config import BOT_TOKEN #BOT_TOKEN="6693715349:AAHja9ojdWnFpeifMAaMn_7tCZdI9bDRIpg"
from aiogram.enums import ParseMode
openai.api_key = "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"

bot=Bot(token=BOT_TOKEN,parse_mode=ParseMode.HTML)
dp=Dispatcher()

@dp.message()
async def echo_message(message:types.Message):
    if message.text:
        def chat_with_bot(prompt):
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message['content'].strip()
        user_input = message.text
        response = chat_with_bot(user_input)
        print("Chatbot:", response)

        await message.answer(text=response)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())