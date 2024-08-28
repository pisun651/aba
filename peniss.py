from telebot import TeleBot
from telebot import types

bot = TeleBot("7292835940:AAFTXBNhLlFt_CFuQchN1QBO-2XdaPanC3k")
chat_id = 12345

button_foo = types.InlineKeyboardButton('Foo', callback_data='foo')
button_bar = types.InlineKeyboardButton('Bar', callback_data='bar')

keyboard = types.InlineKeyboardMarkup()
keyboard.add(button_foo)
keyboard.add(button_bar)

bot.send_message(chat_id, text='Keyboard example', reply_markup=keyboard)
            bot.polling(none_stop=True)