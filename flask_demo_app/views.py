from flask import render_template, request
from my_script import main

from .app import app
from .forms import MyForm

@app.route("/", methods=['GET', 'POST'])
def run_script():
    form = MyForm()
    if request.form:
        output = main(request.form['my_input'])
    else:
        output = ''
    return render_template('flask_template.html',
                           output=output,
                           form=form)
