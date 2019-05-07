import telebot
import predict
from joblib import load

token = "726549055:AAFCjJvi3Y1k7JsyG20EYMqBr0g6KtW1tzM"
bot = telebot.TeleBot(token)

model = load('model.pkl')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    res = predict.headline_processing(message.text, model)
    bot.send_message(message.chat.id, res)

bot.polling(none_stop=True, interval=0)
