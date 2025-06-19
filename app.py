import sqlite3
from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def get_db_connection():
    conn = sqlite3.connect('databse.db')  
    conn.row_factory = sqlite3.Row
    return conn

# Show homepage at '/'
@app.route('/')
def home():
    return render_template('yup.html')

# Show latest submission at '/submission'
@app.route('/submission')
def submission():
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users ORDER BY id DESC LIMIT 1').fetchone()
    conn.close()

    print(user)
    return render_template('index.html', user=user)

#  Form submission route
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']

        if not firstname:
            flash('Firstname is required!')
        elif not lastname:
            flash('Lastname is required!')
        elif not email:
            flash('Email is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO users (firstname, lastname, email) VALUES (?, ?, ?)',
                         (firstname, lastname, email))
            conn.commit()
            conn.close()
            return redirect(url_for('submission'))  #  redirect to /submission

    return render_template('yup2.html')

# Optional: still keep /about
@app.route('/about')
def about():
    return render_template('yup3.html')

if __name__ == '__main__':
    app.run(debug=True)
