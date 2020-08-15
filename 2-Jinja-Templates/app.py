from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"


@app.route('/dateisodd')
def dateisodd():
    current_time = datetime.datetime.now()
    day = current_time.day
    month = current_time.month
    year = current_time.year
    is_odd = day%2
    print(f"date is : {day}")
    return render_template('date.html',is_odd=is_odd,day=day,month=month,year=year)


@app.route('/forloop')
def forloop():
    array = ['Gaurav','Mahesh','Aniket','Dushyant','Omkar','Saurabh']
    return render_template('friends.html',array=array)


if __name__ == '__main__':
    app.run()
