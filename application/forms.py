from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, RadioField, HiddenField
from wtforms.validators import DataRequired, Length, Email, ValidationError, InputRequired
from application.models import User, Comment, Rating


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
    password = PasswordField("Enter your Password", validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Log In")


class UpdateAccountForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=10)])
    email = StringField("Email", validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("That username is taken. Please choose a different one.")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email is taken by another user. Please use a different one.")


class UserFeedback(FlaskForm):  
    # positive_rating = RadioField("Thumbs Up")
    # negative_rating = StringField("Thumbs Down")
    recipe_rating = RadioField("Please choose a rating:", choices=[(1, '1 Star'), (2, '2 Star'), (3, '3 Star'), (4, '4 Star'), (5, '5 Star')])
    comment = TextAreaField("Enter your comments here", validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField("Submit Comment")


class SaveRecipe(FlaskForm):
    user_id = HiddenField("user_id")
    recipe_id = HiddenField("recipe_id")
    submit = SubmitField("Save Recipe")


class DeleteUserFeedback(FlaskForm):
    submit = SubmitField("Delete Comment")

