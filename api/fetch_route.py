from flask import Blueprint
from api.add_route import tax_data

fetch = Blueprint('fetch', __name__)

remove = "<>"


# Вывод списка налоговых ставок
@fetch.route('/v1/fetch/taxes', methods=['GET'])
def fetch_all():
    if tax_data is None:
        error_body = {'reason': 'Список пуст'}
        return error_body, 400
    else:
        return tax_data, 200


# Вывод данных по указанному коду региона
@fetch.route('/v1/fetch/tax/<id>', methods=['GET'])
def fetch_one(id):
    if tax_data is None:
        return '400 BAD REQUEST'
    else:
        if tax_data[id]:
            message = {id: tax_check[id]}
            return message, 200
        else:
            return '400 BAD REQUEST'


# Подсчёт налога
@fetch.route('/v1/fetch/calc/<id>/<month>/<price>', methods=['GET'])
def calc(id, price, month):
    if id is None or price is None or month is None:
        return '400 BAD REQUEST'
    # Удаление лишних символов
    for symbol in remove:
        id = id.replace(symbol, "")
        month = month.replace(symbol, "")
        price = price.replace(symbol, "")
    if tax_data is None:
        return '400 BAD REQUEST'
    else:
        if tax_data[id]:
            res = (int(price) * int(tax_data[id]) * int(month)) / 12
            message = {"res": res}
            return message, 200
        else:
            return '400 BAD REQUEST'
