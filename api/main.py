from flask import Flask
from api.add_route import add
from api.fetch_route import fetch
from api.update_route import update

app = Flask(__name__)

app.register_blueprint(add)
app.register_blueprint(update)
app.register_blueprint(fetch)

if __name__ == '__main__':
    app.run(debug=True)
