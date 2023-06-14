# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    my = "Rithika" # write your name
    age1 = "14" # write your age

    return render_template('index.html' , name = my , age = age1)

# define the route to father webpage
@app.route("/father")
def father():
    dname = "Mahender"
    age2 = "46"

    return render_template('father.html' , name = dname , age = age2)
# define the route to mother webpage
@app.route('/mother')
def mother():
    mname = "Sapna"
    age3 = "Unknown....."
    return render_template('mother.html' , name = mname , age = age3)
# define the route to friends webpage
@app.route('/friend')
def friends():
    bname = "Prithika"
    age4 = "14"
    return render_template('friend.html',name = bname , age = age4)
# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
 
