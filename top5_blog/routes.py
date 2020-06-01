from top5_blog import app
from flask import render_template

@app.route('/')
def home():
    welcome_message = "Welcome!"
    return render_template('home.html')

@app.route('/top5', methods=['GET', 'POST'])
def top5():
    item_dict = {1: "Jim Gaffigan", 2:"Jimmy O. Yang", 3:"Jerry Seinfeld", 4:"Kevin Hart", 5:"Nate Bargatze"}
    return render_template("top5.html", item_dict = item_dict)
