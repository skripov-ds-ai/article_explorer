from flask import Flask
from navigator import app
# app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     print(app.db)
#     return 'Hello World!'
#
#
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
