'''
https://t.me/afande_bot
api token = 5525726835:AAH8QttBCi2PStjS9Ta5i64dPDYtbea_3fE
name = afande
username = afande_bot
'''

import telegram
import telegram.bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='5525726835:AAH8QttBCi2PStjS9Ta5i64dPDYtbea_3fE', use_context=True) 
dispatcher = updater.dispatcher

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Afande reporting for duty.')

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)


print("The bot is currently running!")
updater.start_polling()
