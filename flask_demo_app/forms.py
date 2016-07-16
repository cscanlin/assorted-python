from flask.ext.wtf import Form
from wtforms import StringField

class MyForm(Form):
    my_input = StringField('my_input')
