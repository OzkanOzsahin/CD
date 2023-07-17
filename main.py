from flask import Flask


app = Flask (__name__)

@app.route('/')
def index():
    return b'Hello, welcome to my last assignment'
app.run(port=8080)
