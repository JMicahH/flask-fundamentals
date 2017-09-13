from flask import Flask, render_template, request, redirect, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "hush-hush"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formsubmit', methods = ['post'])
def formsubmit():
    firstname = request.form['first_name']
    lastname = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    passwordconf = request.form['password_confirmation']

    session['firstname'] = firstname
    session['lastname'] = lastname
    session['email'] = email
    session['password'] = password
    session['passwordconf'] = passwordconf
    
    messages = False

    if len(firstname) < 1:
        flash("First Name field must not be blank.", 'blankfield')
        messages = True
    elif not NAME_REGEX.match(firstname):
        print "not a letter"
        flash("First Name field can only contain letters.", 'invalidinput')
        messages = True

    if len(lastname) < 1:
        flash("Last Name field must not be blank.", 'blankfield')
        messages = True
    elif not NAME_REGEX.match(lastname):
        flash("Last Name field can only contain letters.", 'invalidinput')
        messages = True

    if len(email) < 1:
        flash("Email field must not be blank.", 'blankfield')
        messages = True
    elif not EMAIL_REGEX.match(email):
        flash("Email address not valid.", 'invalidinput')
        messages = True
        

    if len(password) < 1:
        flash("Password field must not be blank.", 'blankfield')
        messages = True
    elif len(password) > 8:
        flash("Password cannot be more than 8 characters.", 'blankfield')
        messages = True        
        
    if len(passwordconf) < 1:
        flash("Password Confirmation field must not be blank.", 'blankfield')
        messages = True

    if not password == passwordconf:
        flash("Password and Confirmation do not match", 'invalidinput')
        messages = True



    return redirect('/')


@app.route('/clearform')
def clearform():
    session.clear()
    return redirect('/')


app.run(debug=True)