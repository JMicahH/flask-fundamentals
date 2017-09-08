from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', name="Jay")

@app.route('users/<username>')
def show_user_profile(username):
    print username
    return render_template("user.html")

@app.route('/route/with/<vararg>')
def handler_function(vararg):
    print vararg



app.run(debug=True)