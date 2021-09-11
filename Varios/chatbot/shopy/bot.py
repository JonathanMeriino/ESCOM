#chatbot usando la libreria python-telegram-bot
from telegram.ext import Updater, CommandHandler


def start(updater,context):
    updater.message.reply_text('Hola, humano!')
def pizza(updater,context):
    updater.message.reply_text('Prefiero pizza')



if __name__ == '__main__':
    updater = Updater(token='1967378721:AAENyFbkqcPNh6APtY_FBRe8A-O4UUlZrVY', use_context=True )

    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('pizza',pizza))
    #add handler

    updater.start_polling()
    updater.idle()