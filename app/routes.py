from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import CheckForm
from app.ML import ML
import numpy as np
@app.route('/result_positive', methods=['POST', 'GET'])
def get_positive():
    return render_template('result_positive.html')

@app.route('/result_negative', methods=['POST', 'GET'])
def get_negative():
    return render_template('result_negative.html')

@app.route('/check_result', methods=['POST', 'GET'])
def login():
    form = CheckForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            x_test = np.array([request.form["sex"], request.form["cp"], request.form["rbp"], request.form["sc"], request.form["fbs"], request.form["rer"], request.form["mhra"], request.form["eia"], request.form["oldpeak"], request.form["slope"], request.form["nmv"], request.form["tal"]])
            for i in range(len(x_test)):
                if (len(x_test[i]) > 1 and x_test[i][1] == '-'):
                    x_test[i] = float(x_test[i][:1])
                else:
                    x_test[i] = int(x_test[i])
            algo = ML()
            x_test = x_test.reshape(1, -1)
            res = algo.predict(x_test)
            print("Ok3")
            if (res[0] == 1):
                return render_template('result_positive.html',  title='Positive_negative')
            else:
                return render_template('result_negative.html',  title='Result_negative')
    return render_template('check.html',  title='Check Form', form=form)
