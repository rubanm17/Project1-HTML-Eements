from flask import Flask, request, render_template
import mysql.connector
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    msg=''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Flask_login"
        )

        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM LoginDetails WHERE Name=%s AND Password=%s', 
                        (username, password)
        )
        
        account = mycursor.fetchone()

        if account:
            name = account[1]
            id = account[0]
            msg = 'Logged in successfully!'
            return render_template('welcome.html', name=name, id=id, msg=msg)
        else:
            msg = 'Incorrect Credentials'

    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    return render_template('login.html', msg='Logged out successfully!')