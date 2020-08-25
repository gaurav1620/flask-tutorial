import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:password@localhost/company")
db = scoped_session(sessionmaker (bind = engine))

# create the company databse from https://github.com/gaurav1620/mysql-basics

def main():
    #names = db.execute("SELECT first_name, last_name, sex, salary, FROM employee;")
    names = db.execute("SELECT first_name, last_name, sex,salary,branch_name FROM employee JOIN branch ON employee.branch_id = branch.branch_id;")

    sex = {}
    sex["M"] = "Male"
    sex["F"] = "Female"
    for fn,ln,sx,sal,bid in names:
        sex = {}
        sex['M'] = "Male"
        sex['F'] = "Female"
        print(f"{fn} {ln} is a {sex[sx]}, is from {bid} branch and has a salary of {sal}.")
main()


'''
OUTPUT : 

David Wallace is a Male, is from Corporate branch and has a salary of 250000
Jan Levinson is a Female, is from Corporate branch and has a salary of 110000
Michael Scott is a Male, is from Scranton branch and has a salary of 75000
Angela Martin is a Female, is from Scranton branch and has a salary of 63000
Kelly Kapoor is a Female, is from Scranton branch and has a salary of 55000
Stanley Hudson is a Male, is from Scranton branch and has a salary of 69000
Josh Porter is a Male, is from Stamford branch and has a salary of 78000
Andy Bernard is a Male, is from Stamford branch and has a salary of 65000
Jim Halpert is a Male, is from Stamford branch and has a salary of 71000
'''
