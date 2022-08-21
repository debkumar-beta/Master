from telegram.ext import *
import pyttsx3
from gtts import gTTS
import keys
from lib2to3.pgen2 import token



print('Starting up bot...')

token = 'Enter your token from telegram godfather bot'
# Lets us use the /start command


def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. What\'s up?')
    update.message.reply_text("""
     Hey Here are some rules:
      1) All mp3 saved as New.mp3
      2)Just Paste or type your stuff it will be converted to mp3
      3)It is in under Devolopment Stay tuned for best version 2.0.0
      4)Devoloped by Deb Kumar Das
                              
                              """)


def help_command(update, context):
    update.message.reply_text(
        'Try typing anything and I will do my best to respond!')


def custom_command(update, context):
    update.message.reply_text(
        'This is a custom command, you can add whatever text you want here.')


def handle_response(text) -> str:

    if 'hello' in text:
        return 'Hey Deb here!'

    if 'how are you' in text:
        return 'I\'m good!'

    else:
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")[0]
        engine.setProperty('voice', voices)
        engine. setProperty("rate", 178)
        engine.save_to_file(text, 'New.mp3')
        engine.runAndWait()


def handle_message(update, context):

    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    if message_type == 'group':

        if '@Textmp3newbot' in text:
            new_text = text.replace('@Textmp3newbot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    update.message.reply_text(response)


def error(update, context):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(1.0)
    updater.idle()
