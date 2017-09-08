from flask import Flask, render_template, request, redirect

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja/')
def ninja():
    return render_template('index.html', turtle='tmnt')

@app.route('/ninja/<color>')
def ninjacolor(color):
    ninjacolors = {'blue':'leonardo',
                   'orange': 'michelangelo', 
                   'red': 'raphael',
                   'purple':'donatello'}

    if color not in ninjacolors:
        turtle = "notapril"

    else:     
        turtle = ninjacolors[color]

    return render_template('index.html', turtle = turtle   )
    
app.run(debug=True)