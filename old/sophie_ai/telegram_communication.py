import telebot
from config import TELEGRAM_API_KEY

class TelegramCommunication:
    def __init__(self):
        self.bot = telebot.TeleBot(TELEGRAM_API_KEY)

    def send_message(self, chat_id, message):
        self.bot.send_message(chat_id, message)

    def receive_message(self, handler_function):
        @self.bot.message_handler(func=lambda message: True)
        def handle_messages(message):
            handler_function(message.chat.id, message.text)

        self.bot.polling()