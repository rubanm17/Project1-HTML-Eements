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
            password="12345",
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Flask_login"
        )

        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM LoginDetails WHERE Name=%s OR Email=%s', (username, email))
        account = mycursor.fetchone()

        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            mycursor.execute('INSERT INTO LoginDetails (Name, Password, Email) VALUES (%s, %s, %s)', 
                            (username, password, email))
            mydb.commit()
            msg = 'You have successfully registered!'

    return render_template('register.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)