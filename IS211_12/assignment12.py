from flask import Flask
from flask import render_template
from flask import url_for, redirect
from flask import request
import sqlite3


app = Flask(__name__)

 
def init():
    database = None
    with open(".\\IS211_12\IS211_schema.sql", "r") as schema:
        database = schema.read()
    conn = sqlite3.connect('IS211_hw12.db')
    cur = conn.cursor()
    cur.executescript(database)
    

def get_db_connection():
    
    conn = sqlite3.connect('IS211_hw12.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=['POST', 'GET'])
def login(): 
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        if (username == 'admin' and password == 'password'):
            return redirect(url_for("showstudents"))
        else:
            return redirect(url_for('login'))
    return render_template('login.html') 
    
@app.route('/showstudents')
def showstudents():
    conn = get_db_connection()
    students = conn.execute('SELECT student_id, student_firstname, student_lastname FROM students')
    quizzes = conn.execute('SELECT quiz_id, subject, num_questions, quiz_date FROM quizzes')
    return render_template('showstudents.html', students=students, quizzes=quizzes)


@app.route("/searchstudent", methods=['POST', 'GET'])
def search_student():
    if request.method == 'POST':
        conn = get_db_connection()
        student_id = request.form['student_id']
        students = conn.execute('SELECT student_id, student_firstname, student_lastname FROM students where student_id = ?', (student_id,))
        return render_template('showstudents.html', students=students)

    return render_template("searchstudent.html")


if __name__ == "__main__":
    app.run(debug=True)
    init()