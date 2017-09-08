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
    session['userguess'] = int(request.form['numberguess'])
    
    if session['userguess'] > session['magicnumber']:
        print "Too high here"
        session['message'] = 'toohigh'
    elif session['userguess'] < session['magicnumber']:
        print "Too low here"
        session['message'] = 'toolow'
    else:
        print "right on"    
        session['message'] = 'guessedright'

    print "magic number is", session['magicnumber']
    print "User guessed", session['userguess']
    print session['message']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('index.html', message = session['message'])


app.run(debug=True)