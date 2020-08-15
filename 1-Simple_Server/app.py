from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/usetemplate')
def temp():
    return render_template("index.html")

@app.route('/passvar')
def passvar():
    return render_template("hello.html",name="Joe")

@app.route('/hello/<string:name>')
def sayhello(name):
    return render_template("hello.html",name=name)


if __name__ == '__main__':
    app.run()
