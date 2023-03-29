import telebot
from Config2 import currencies, TOKEN
from Extensions2 import APIException, CurrenciesConversion

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start(message: telebot.types.Message):
    text = '''Это калькулятор для конвертации валют. Введите команду в формате:
    <валюта, из которой переводим> <валюта, в которую переводим> <количество первой валюты>
    Например: доллар рубль 100
    Курсы валют определяются сервисом exchangerate.host.
    Посмотреть список досутпных валют можно по команде /values'''
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def handle_values(message: telebot.types.Message):
    text = ''
    for key in currencies.keys():
        text = '\n'.join((text, key))
    text = f"Список доступных валют:\n {text}"
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def curr_converter(message: telebot.types.Message):
    try:
        params = message.text.split()
        if len(params) != 3:
            raise APIException("Команда должна содержать ровно 3 параметра.")

        base, quote, amount = params
        total_out, base_out, quote_out, amount_out = CurrenciesConversion.get_price(base, quote, amount)
        text = f"{amount_out} {base_out} - это {total_out} {quote_out}"

    except APIException as e:
        text = f"Ошибка ввода. {e}"

    finally:
        bot.reply_to(message, text)


bot.polling(none_stop=True)