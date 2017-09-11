from flask import Flask, redirect, render_template, session, request

import random

app = Flask(__name__)
app.secret_key = "secretSecret"

@app.route('/')
def index():
    if not session.get('activity'):
        session['totalgold'] = 0
        print "totalgold initialized"
        session['activity'] = []
        print "activity initialized", session['activity']

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    location = request.form['building']
    print "processgold start: " + str(session['totalgold'])
    if location == 'farm':
        gold = random.randrange(10, 21)
        session['totalgold'] += gold
        session['activity'].append("You earned " + str(gold) + " gold at the Farm.")
        
    elif location == 'cave':
        gold = random.randrange(5, 11)
        session['totalgold'] += gold
        session['activity'].append("You earned " + str(gold) + " gold at the Cave.")


    elif location == 'house':
        gold = random.randrange(2, 6)
        session['totalgold'] += gold
        session['activity'].append("You earned " + str(gold) + " gold at the House.")

    elif location == 'casino':
        if session['totalgold'] == 0:
            session['activity'].append("You don't have enough gold to play at the Casino.")
            session.modified = True
            print "AFTER", session['activity']
        else:
            gold = random.randrange(50)
            winorlose = random.randrange(2)
            if winorlose >= 1:
                session['totalgold'] += gold
                session['activity'].append("You won " + str(gold) + " gold at the Casino.")
            else:
                if gold <= session['totalgold']:
                    session['totalgold'] -= gold 
                else:
                    session['totalgold'] = 0
                session['activity'].append("You lost " + str(gold) + " gold at the Casino.")            

    return redirect('/')

@app.route('/cleargold')
def cleargold():
    session.clear()
    return redirect('/')


app.run(debug=True)