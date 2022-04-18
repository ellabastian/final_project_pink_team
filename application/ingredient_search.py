from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class IngredientsForm(FlaskForm):
    ingredients = StringField("Enter ingredients")
    submit = SubmitField("Search")
