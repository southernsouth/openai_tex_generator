import telebot
import openai
import json

with open('config.json', 'r') as f:
    cfg = json.load(f)


bot = telebot.TeleBot(cfg['bot_token'])
openai.api_key = cfg['api_key']

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = "Hi, I'm a bot to help you with answers to your questions"
    bot.send_message(message.chat.id, text=text)

@bot.message_handler(content_types=['text'])
def func(message):
    data = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You're a Telegram bot that helps with answers to questions"},
        {"role": "user", "content": message.text}
        ])

    text = data['choices'][0]['message']['content']
    bot.send_message(message.chat.id, text=text)

print("Bot started")
bot.infinity_polling()
