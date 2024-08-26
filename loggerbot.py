# СОЗДАТЕЛЬ ЭТОГО БОТА @exploitwizard
#слито в @pr0xit

import telebot
from telebot import types

bot = telebot.TeleBot('7292835940:AAFTXBNhLlFt_CFuQchN1QBO-2XdaPanC3k')

@bot.message_handler(commands=['start'])
def register(message):
keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
reg_button = types.KeyboardButton(text="Share your phone number", request_contact=True)
keyboard.add(reg_button)

@bot.message_handler(content_types=['contact'])
def contact_handler(message):
print(message.contact.phone_number)

if __name__ == '__main__':
bot.polling(none_stop=True)



# СОЗДАТЕЛЬ ЭТОГО БОТА @exploitwizard
#слито в @pr0xit
