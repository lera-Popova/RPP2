from flask import Blueprint, request
from api.add_route import tax_data

update = Blueprint('update', __name__)


# Обновление данных в коллекции
@update.route('/v1/update/tax', methods=['POST'])
def tax_update():
    id = request.json['id']
    tax = request.json['tax']
    if tax_data[id]:
        tax_data[id] = tax
        return tax_check, 200
    else:
        return '400 BAD REQUEST'