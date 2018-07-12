from flask import Flask, render_template, redirect, url_for, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guss string'

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, validators
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

class loginForm(FlaskForm):
    userName = StringField(validators=[Required()])
    passWord = passwordField(validators=[Required()])
    submit = SubmitField('login')

#database query
from db import db, User

@app.route('/', methods=['GET', 'POST'])
def index():
    if loginform.validate_on_submit():
        return redirect(url_for(''))
    else:
        pass

    return render_template('index.html', form = searchForm)

if __name__ =='__main__':
    app.run(debug=True)
