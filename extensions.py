import requests
import json
from Token import keys

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base:str, quote:str, amount:float):

        if quote == base:
            raise ValueError('Невозможно конвертировать валюту в саму себя')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}, проверьте корректность ввода')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}, проверьте корректность ввода')

        try:
            # Проверка типа amount
            if not isinstance(amount, (int, float)):
                raise ValueError('Сумма должна быть числом')

            req = requests.get(
                f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}'
            )
            req.raise_for_status()  # Проверка статуса ответа

            data = req.json()
            rate = float(data[quote_ticker])
            total_base = rate * amount

            return total_base

        except requests.exceptions.HTTPError as http_error:
            raise APIException(f'HTTP ошибка: {http_error}')

        except requests.exceptions.ConnectionError as connect_err:
            raise APIException(f'Ошибка подключения: {connect_err}')

        except ValueError as ve:
            raise APIException(f'Ошибка преобразования: {ve}')

