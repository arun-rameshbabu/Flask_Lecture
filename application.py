from flask import Flask, redirect, url_for, request, render_template
from forms import BeneficiaryForm
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asfhdasfhbakwjbkfefr7y57y47rjbfkabzfcbhafbka'

@app.route('/')
def hello_world():
    """
    Function to show example instance
    :return:
    """
    return render_template('index.html')

@app.route('/add_beneficiary', methods = ['POST', 'GET'])
def add_beneficiary():
    """
    Function to show example instance
    :return:
    """
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        print(fname, lname)
        return "Beneficiary added successfully"
    else:
        return render_template('add_beneficiary_manual.html')

@app.route('/add_beneficiary_auto', methods = ['POST', 'GET'])
def add_beneficiary_auto():
    """
    Function to show example instance
    :return:
    """
    form = BeneficiaryForm()
    if form.validate_on_submit():
        applicant_name = form.applicant_name.data
        applicant_email = form.applicant_email.data
        applicant_tel = form.applicant_tel.data
        applicant_dob = form.applicant_dob.data
        applicant_desc = form.applicant_desc.data
        df = pd.DataFrame([{'name': applicant_name, 'email': applicant_email, 'tel': applicant_tel, 'dob':applicant_dob, 'desc':applicant_desc}])
        print(df)
        return redirect(url_for('hello_world'))
    else:
        return render_template('add_beneficiary_auto.html', form=form)

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

@app.route('/input', methods = ['POST', 'GET'])
def information():
    if request.method == 'POST':
        info = request.form['info']
        return redirect(url_for('hello_guest', guest=info))
    else:
        return redirect(url_for('hello_world'))

@app.route('/texample')
def table_example():
    username = 'Michael'
    avg_score = 70
    marks_dict = {'phy': 50, 'che': 70, 'math': 90}
    return render_template('texample.html', name = username, marks = avg_score, results = marks_dict)


if __name__ == '__main__':
    app.run(debug=True)