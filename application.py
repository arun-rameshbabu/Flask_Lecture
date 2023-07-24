from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
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

if __name__ == '__main__':
    app.run(debug=True)