from aiogram import types, Dispatcher
import logging
from create_bot import dp, bot

import logging
from aiogram import Bot, Dispatcher, types

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import requests
from aiogram.types import ParseMode


import requests







import requests


url_kb_group = InlineKeyboardMarkup(row_width=1)
urlButton2 = InlineKeyboardButton(text='ბილეთები', url='https://t.me/ticketthriftmarket')
urlButton3 = InlineKeyboardButton(text='ბილეთის ყიდვის წესი', callback_data='ticket_buy_rules')
url_kb_group.add(urlButton2, urlButton3)


API_TOKEN = 'your_telegram_bot_token'
BOT_URL = 'your_bot_webhook_url'  # Set up a webhook and provide the URL here

logging.basicConfig(level=logging.INFO)


# Command to start the bot
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_id, "gamarjoba")

    





















def register_handlers_Firstpage(dp : Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])


