from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

notes = []

@app.route('/',methods=["GET", "POST"])
def index():
    if request.method == "POST":
        notes.append([request.form.get("title"),request.form.get("note")])

    return render_template('index.html',notes=notes)

if __name__ == '__main__':
    app.run()
