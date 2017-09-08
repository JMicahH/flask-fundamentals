from flask import Flask, redirect, render_template, session, request

import random
app = Flask(__name__)
app.secret_key = "secretSecret"

@app.route('/')
def index():
    session.pop('magicnumber')
    session['magicnumber'] = random.randrange(0, 101)
    print "magic number is", session['magicnumber']
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    userguess = int(request.form['numberguess'])
    print type(userguess)
    
    if userguess > session['magicnumber']:
        print "Too high here"
        message = 'toohigh'
    elif userguess < session['magicnumber']:
        print "Too low here"
        message = 'toolow'
    else:
        print "right on"    
        message = 'guessedright'

    print "magic number is", session['magicnumber']
    print "User guessed", userguess
    print message

    return render_template('index.html', message = message)



app.run(debug=True)