from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Function to show example instance
    :return:
    """
    return 'Hello World'

@app.route('/variabletest/<name>')
def print_variable(name):
    return 'Hello %s!' % name

@app.route('/integertest/<int:intID>')
def print_integer(intID):
    return 'Number %d!' % intID

@app.route('/floattest/<float:floatID>')
def print_float(floatID):
    return 'Floating Number %f!' % floatID

@app.route('/admin')
def hello_admin():
    return "Hello Admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello % as Guest" % guest

@app.route('/user/<user>')
def hello_user(user):
    if user=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=user))

if __name__ == '__main__':
    app.run(debug=True)