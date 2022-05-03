from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, HiddenField, RadioField, widgets
from wtforms.validators import DataRequired, Length, Email, ValidationError
from application.models import User, Comment, Rating


class IngredientsForm(FlaskForm):
    ingredients = StringField("Enter an ingredient:")
    submit = SubmitField("Search Recipes")


class UserAccountForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    username = StringField("Create a Username for your account", validators=[DataRequired(message="Please enter a username"), Length(min=4, max=10)])
    email = StringField("Enter your e-mail address", validators=[DataRequired(), Email(message="Check the format of your email address")])
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
    email = StringField("Enter your e-mail address", validators=[DataRequired(), Email()])
    password = PasswordField("Enter your Password", validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Log In")


class UpdateAccountForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=10)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
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
    user_id = HiddenField("user_id")
    recipe_id = HiddenField("recipe_id")
    recipe_rating = RadioField("Please choose a rating", choices=[(1, '1 Star'),(2, '2 Star'), (3, '3 Star'),
                                                                  (4, '4 Star'), (5, '5 Star')])
    comment = TextAreaField("Enter your comments here", validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField("Submit Comment")


class DeleteUserFeedback(FlaskForm):
    submit = SubmitField("Delete Comment")


class SaveRecipe(FlaskForm):
    user_id = HiddenField("user_id")
    recipe_id = HiddenField("recipe_id")
    submit = SubmitField("Save Recipe")


class ViewRecipes(FlaskForm):
    submit = SubmitField("View Recipes")