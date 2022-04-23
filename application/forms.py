from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from application.models import User


class IngredientsForm(FlaskForm):
    ingredients = StringField("Enter an ingredient:")
    submit = SubmitField("Search Recipes")


class UserAccountForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    username = StringField("Create a Username for your account", validators=[DataRequired(), Length(min=4, max=10)])
    email = StringField("Enter your e-mail address", validators=[DataRequired()])
    password = PasswordField("Create a Password for your account", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken. Please choose a different one.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken by another user. Please use a different one.")


class UserLoginForm(FlaskForm):
    email = StringField("Enter your e-mail address", validators=[DataRequired()])
    password = StringField("Enter your Password", validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Log In")

