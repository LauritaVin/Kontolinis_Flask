from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError, Regexp
import app
import re


class RegisterForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [DataRequired(), Email()]) #patikrina tiesiog baisc email formata
    password = PasswordField('Password', [DataRequired()])
    confirm_password = PasswordField(
        'Repeat password', [DataRequired(), EqualTo('password', 'Passwords must match')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        if not re.match(r'^[\w\.-]+@gmail\.com$', email.data):
            raise ValidationError('Wrong email type, please use name@gmail.com') #tikrina ar po @ eina 'gmail', o ne random raides (galimas tobulinimas, kad priimtu ir kitu tipu email - yahoo ir pan.)
        with app.app.app_context():
            user = app.User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is already in use')

    def validate_name(self, name):
        with app.app.app_context():
            user = app.User.query.filter_by(name=name.data).first()
            if user:
                raise ValidationError('This name is already in use')


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class EntryForm(FlaskForm):
    income = BooleanField('Income')
    sum = FloatField('Sum', [DataRequired()])
    submit = SubmitField('Submit')

class ChangeForm(FlaskForm):
    email = StringField('Email', [DataRequired()])
    name = StringField('Name', [DataRequired()])
    submit = SubmitField('Atnaujinti')
