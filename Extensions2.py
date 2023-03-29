import requests
import json
from Config2 import currencies

class APIException(Exception):
    pass
def search_curr_name(name: str):
    """Функция пытается найти среди ключей или исправить название валюты, чтобы представить ее в том же виде, в каком
    валюты записаны в ключах словаря currencies"""
    name = name.lower()
    if name in currencies.keys():
        return name
    else:
        # Проверяем в цикле, не найдется ли введенное пользователем слово среди альтернативных имен валют
        for curr in currencies.keys():
            if name in currencies[curr][2]:
                return curr
        # Если ничего не нашлось, выдаем ошибку
        raise APIException(f"Не удалось обработать валюту <{name}>.\nСписок доступных валют указан по команде /values")


class CurrenciesConversion():
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        base = search_curr_name(base)
        base_code = currencies[base][0]

        quote = search_curr_name(quote)
        quote_code = currencies[quote][0]

        try:
            # Преобразовываем строку в число, исправив возможную ошибку - десятичный разделитель (запятую)
            # и отрицательную сумму
            amount = abs(float(amount.replace(',', '.'))) # если пользователь ввел разделительную запятую вместо точки
        except ValueError:
            raise APIException(f"Не удалось обработать сумму {amount}.")

        r = requests.get(f'https://api.exchangerate.host/convert?from={base_code}&to={quote_code}')
        total_base = r.json()['result'] * amount

        return round(total_base, 2), currencies[base][1], currencies[quote][1], amount