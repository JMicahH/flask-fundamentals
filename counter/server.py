from flask import Flask, redirect, render_template, session

app=Flask(__name__)
app.secret_key = "secretSecret"

@app.route('/')
def index():
    session['count'] += 1
    return render_template('index.html', count = session['count'])

@app.route('/plus2/')
def plus2():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)