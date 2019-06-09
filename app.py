from flask import Flask
from recommendation import rec_app

app = Flask(__name__)
app.register_blueprint(rec_app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
