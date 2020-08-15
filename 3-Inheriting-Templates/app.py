from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/bye')
def bye():
    return render_template('bye.html')

if __name__ == '__main__':
    app.run()
