import constants as keys 
from telegram.ext import *
import respuestas as R

print("Bot inicializado")

def start_command(update,context):
    update.message.reply_text('Listo para iniciar la conversacion')

def help_command(update,context):
    update.message.reply_text('Intenta decir "Hola" \n Vamos, no seas timido ')


def handle_message(update,context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    respuestas = R.evaluacion(text)

    update.message.reply_text(response)
    update.message.reply_text(respuestas)


def error(update,context):
    print(f"Actualizacion {update } error causado{context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True )
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))

    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_error_handler(error)


    updater.start_polling(5)
    updater.idle()

main()