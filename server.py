from flask import Flask, redirect, request, session, render_template, flash
import re
app = Flask(__name__)
app.secret_key = "WowowowSecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9.!]+$')


@app.route('/')
def root():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    error = False
    if len(request.form['email']) < 1:
        flash("You must enter an email!")
        error = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email!")
        error = True
    if len(request.form['first_name']) < 1:
        flash("Must enter a name!")
        error = True
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("Must enter a valid name!")
        error = True
    if len(request.form['last_name']) < 1:
        flash("Must enter a name!")
        error = True
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Must enter a valid name!")
        error = True
    if request.form['password'] == request.form['password_confirm']:
        if len(request.form['password']) < 8:
            flash("Password is too short!")
            error = True
        elif not PASSWORD_REGEX.match(request.form['password']):
            flash("Invalid password")
            error = True
        if not any (char.isdigit() and not any (char.isupper() for char in request.form['password']) for char in request.form['password']):
            flash("Your password must have atleast one uppercase and number")
            error = True
    else:
        error = True
    if error == False:
        flash("Everything is working fine. Thank you.")
    return redirect('/')

app.run(debug=True)