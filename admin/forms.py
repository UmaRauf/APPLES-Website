import re
from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


# Custom validator to check for invalid characters
def validate_no_special_characters(form, field):
    if re.search(r'[<>&%]', field.data):
        raise ValidationError("Field must not contain the characters <, &, or %.")


# Custom validator to check for a digit in the password
def validate_digit(form, field):
    if not re.search(r'\d', field.data):
        raise ValidationError("Password must contain at least one digit.")


# Custom validator to check for a lowercase character in the password
def validate_lowercase(form, field):
    if not re.search(r'[a-z]', field.data):
        raise ValidationError("Password must contain at least one lowercase letter.")


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Email(),
        validate_no_special_characters
    ])

    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, max=15),
        validate_no_special_characters,
        validate_digit,
        validate_lowercase
    ])

    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message="Passwords must match")
    ])

    submit = SubmitField('Register')

def no_special_characters(form, field):
    if any(char in field.data for char in '<&%'):
        raise ValidationError('Field must not contain <, &, or % characters.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Email(), no_special_characters])
    password = PasswordField('Password', validators=[DataRequired(), no_special_characters])
    recaptcha = RecaptchaField()
    submit = SubmitField('Login')

class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_new_password = PasswordField('Confirm New Password',
                                         validators=[DataRequired(),
                                                     EqualTo('new_password', message='Passwords must match')])
    submit = SubmitField('Change Password')