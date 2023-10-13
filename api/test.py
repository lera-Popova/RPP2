from flask import Flask
app = Flask(__name__)
@app.route('/v1/test')
def test():
    return 'Ok'
if __name__=='__main__':
    app.run()