from flask import Flask, render_template, request, redirect, session

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
    return redirect('/userdisplay')

@app.route('/userdisplay')
def userdisplay():
    return render_template('result.html')

@app.route('/gohome')
def gohome():
    return redirect('/')


app.run(debug=True)

