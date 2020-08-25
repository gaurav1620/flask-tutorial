from flask import Flask, render_template, request
import datetime
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:password@localhost/company")
db = scoped_session(sessionmaker (bind = engine))

app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def index():
    if request.method == "GET":
        dat = db.execute("SELECT first_name, last_name, sex,salary,branch_name FROM employee JOIN branch ON employee.branch_id = branch.branch_id;")
    
    return render_template('index1.html',data=dat,)

if __name__ == '__main__':
    app.run()
