from flask import Flask,redirect, render_template, request, url_for
import datetime
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:password@localhost/notes")
db = scoped_session(sessionmaker (bind = engine))

app = Flask(__name__)

@app.route('/delnote/',methods=["POST"])
def delnote():
    m = "Done !"
    if request.method == "POST":
        try:
            if(db.execute("SELECT * FROM notes WHERE id = (:id);",{"id":request.form.get("id")}).fetchone() == None):
                m = "ERROR: Note with given id not found!"
                print(m)
            else :
                db.execute("DELETE FROM notes WHERE id = (:id);",{"id":request.form.get("id")})
                db.commit()
        except :
            m = "ERROR while deleting a record !"
            print(m)
    return redirect(url_for("index",mess = m))


@app.route('/',methods=["GET", "POST"])
def index(mess = "Empty"):
    m = "Done !"
    if request.method == "POST":

        title = request.form.get("title")
        body = request.form.get("body")

        # due date is str
        due_date = request.form.get("dd")
        # dur time is str
        due_time = request.form.get("dt")
        
        print("************* Adding a new Note ************")
        print("Title  : ",title)
        print("Body   : ",body)
        due_at = due_date + " " + due_time + ":00"
        print("Due at : ",due_at)


        try:
            db.execute("INSERT INTO notes(title, body, due_at) VALUES(:title, :body, :due_at);",{"title":title, "body": body, "due_at": due_at})
            db.commit()
        except :
            m = "ERROR occured while adding a new record !"
            print(m)
    
        print("Done querying !")
    if request.args.get("mess") != None:
        m = request.args.get("mess")
    dat = db.execute("SELECT id, title, body, created_at, due_at FROM notes;")
    return render_template('index.html',data=dat,mess=m)

if __name__ == '__main__':

    app.run()


'''
DATABSE SCHEMA: 

mysql> describe notes;
+------------+---------------+------+-----+-------------------+----------------+
| Field      | Type          | Null | Key | Default           | Extra          |
+------------+---------------+------+-----+-------------------+----------------+
| id         | int(11)       | NO   | PRI | NULL              | auto_increment |
| title      | varchar(100)  | NO   |     | NULL              |                |
| body       | varchar(1000) | YES  |     | NULL              |                |
| created_at | timestamp     | NO   |     | CURRENT_TIMESTAMP |                |
| due_at     | timestamp     | NO   |     | CURRENT_TIMESTAMP |                |
+------------+---------------+------+-----+-------------------+----------------+
'''
