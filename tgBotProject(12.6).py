import telebot
from Token import TOKEN, keys
from extensions import APIException, Converter

token = TOKEN

API = 'PZtwd4uOqhIt0IjYlBhwWAXHJ6bCBYk0'
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start', 'help', 'values'])
def msg_command (message: telebot.types.Message):
    if message.text == '/help':
        text = 'Введите имя конвертируемой валюты, \
            введите имя валюты в которую необходимо конвертировать, \
            количество первой валюты'
        bot.reply_to(message, text)
    if message.text == '/start':
        text = 'Привет! Какую валюту будем искать?'
        bot.reply_to(message, text)
    if message.text == '/values':
        values(message)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert (message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Требуется ввести три параметра')
        base, quote, amount = values
        amount = float(amount)
        total_base = Converter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()