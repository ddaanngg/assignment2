from flask import Flask, render_template, jsonify

app = Flask(__name__)

#create the home page
@app.route('/')
def index():
    return render_template('home.html')

#create a page for my birthday
@app.route('/birthday')
def birthday():
    birthday = 'August 27, 1991'
    return birthday

#create the greeting page
@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name + '!'

#add 2 numbers
@app.route('/add/<int:parameter1>/<int:parameter2>')
def add(parameter1, parameter2):
    sumOfParameters = str(parameter1 + parameter2)
    return str(parameter1) + ' + ' + str(parameter2) + ' = ' + sumOfParameters

#multiply numbers
@app.route('/multiply/<int:parameter1>/<int:parameter2>')
def multiply(parameter1, parameter2):
    productOfParameters = str(parameter1 * parameter2)
    return str(parameter1) + ' x ' + str(parameter2) + ' = ' + productOfParameters

#subtract 2 numbers
@app.route('/subtract/<int:parameter1>/<int:parameter2>')
def subtract(parameter1, parameter2):
    sumOfParameters = str(parameter1 - parameter2)
    return str(parameter1) + ' - ' + str(parameter2) + ' = ' + sumOfParameters

#providing a list of your favorite foods
@app.route('/list/<food1>/<food2>/<food3>')
def list(food1, food2, food3):
    myList = [str(food1), str(food2), str(food3)]
    return jsonify(myList)
