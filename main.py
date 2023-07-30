from flask import Flask


app = Flask (__name__)

@app.route('/')
def index():
    return b'Hello, world, i am getting lost!'



