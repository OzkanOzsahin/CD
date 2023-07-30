from flask import Flask


app = Flask (__name__)

@app.route('/')
def index():
    return b'Hello, i am testing and testing!'




