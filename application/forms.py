from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class IngredientsForm(FlaskForm):
    ingredients = StringField("Enter ingredients")
    submit = SubmitField("Search Recipes")


class UserAccountForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    username = StringField("Create a Username for your account")
    email = StringField("Enter your e-mail address")
    password = StringField("Create a Password for your account. This must be 8 characters long")
    submit = SubmitField("Register")

