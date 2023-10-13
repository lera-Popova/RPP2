from flask import Blueprint, request

add = Blueprint('add', __name__)

tax_data = {}


# добавление значения в список
@add.route('/v1/add/tax', methods=['POST'])
def add_new():
    id = request.json['id']
    tax = request.json['tax']
    if id in tax_data:
        return '400 DAD REQUEST'
    else:
        tax_data[id] = tax
        return {}, 200
