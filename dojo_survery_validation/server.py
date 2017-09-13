from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "SecretSecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['dojoloc'] = request.form['dojoloc']
    session['favlang'] = request.form['favlang']
    session['comment'] = request.form['comment']
    messages = False
    if len(session['name']) < 1:
        print "Name field", len(session['name'])
        flash("Name field cannot be empty.")
        messages = True

    elif len(session['comment']) < 1:
        flash("Comment field cannot be empty.")
        messages = True

    elif len(session['comment']) > 121:
        flash("Comment field cannot contain more than 120 characters.")
        messages = True
    if messages:
        return redirect('/')
    else:
        return redirect('/userdisplay')

@app.route('/userdisplay')
def userdisplay():
    return render_template('result.html')

@app.route('/gohome')
def gohome():
    session.clear()
    return redirect('/')


app.run(debug=True)

