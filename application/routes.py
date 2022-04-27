import os
import secrets
from PIL import Image
from flask import render_template, request, url_for, redirect, flash
from application import app, db, bcrypt
from application.forms import IngredientsForm, UserAccountForm, UserLoginForm, UpdateAccountForm, UserFeedback
from application.models import Ingredient, IngredientRecipe, Recipe, Instruction, Difficulty, User, Comment
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/home", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():
    error = ""
    form = IngredientsForm()

    if request.method == "POST":
        ingredient_result = form.ingredients.data

        if len(ingredient_result) == 0:
            error = "Please supply an ingredient"

        elif Ingredient.query.filter_by(ingredient_name=ingredient_result).first() == None:
            error = "Try another ingredient"
        else:
            ingredient_id = (Ingredient.query.filter_by(ingredient_name=ingredient_result).first()).ingredient_id
            recipe_ids = (IngredientRecipe.query.filter_by(ingredient_id=ingredient_id).all())
            recipes = []
            for ingredient_id in recipe_ids:
                recipe_id = ingredient_id.recipe_id
                recipes.extend(Recipe.query.filter_by(recipe_id=recipe_id).all())
            return render_template('recipe.html', ingredient_id=ingredient_id, recipes=recipes)

    return render_template('home.html', form=form, message=error)


@app.route("/recipes/<recipe_name>", methods=["GET", "POST"])
def specific_recipe(recipe_name):
    # form = UserFeedback()
    recipe = (Recipe.query.filter_by(recipe_name=recipe_name).first())
    instructions = Instruction.query.filter_by(recipe_id=recipe.recipe_id).all()
    # return render_template('specific_recipe.html', recipe_name=recipe_name, recipe=recipe, instructions=instructions, form=form)

    form = UserFeedback()
    if form.validate_on_submit():
        comment_query = Comment(comment=form.comment.data)
        db.session.add(comment_query)
        db.session.commit()
        list_of_comments = Comment.query.all()
        return render_template('specific_recipe.html', form=form, comment=form.comment.data, recipe=recipe, list_of_comments=list_of_comments, current_user=current_user.id)
    return render_template('specific_recipe.html', recipe_name=recipe_name, recipe=recipe, instructions=instructions, form=form, current_user=current_user.username)

    # # form = UserFeedback()
    # # if request.method == "POST":
    # #     # positive_rating = form.positive_rating.data
    # #     # negative_rating = form.negative_rating.data
    # #     usercomment = form.comment.data
    # #
    # #     if current_user.is_authenticated:
    # #         # username = User.query.get("username")
    # #         # recipe_id = Recipe.query.get("recipe_id")
    # #         # commentquery = Comment.insert().values({"comment": usercomment}, recipe_id=recipe_id, username=username)
    # #         comment_query = Comment(comment=usercomment)
    # #         db.session.add(comment_query)
    # #         db.session.commit()
    # #         return render_template('specific_recipe.html', comment=usercomment, comment_query=comment_query, form=form)
    # #
    # #     else:
    # #         return redirect(url_for('user_account'))
    # # return render_template('specific_recipe.html', recipe_name=recipe_name, recipe=recipe, instructions=instructions, form=form)
    #
    # form = UserFeedback()
    # if request.method == "POST":
    #     user_comment = form.comment.data
    #     # comment_query = Comment(comment=user_comment, id=1, recipe_id=2)
    #     # db.session.add(comment_query)
    #     # db.session.commit()
    #     # return render_template('specific_recipe.html', user_comment=user_comment, comment_query=comment_query, id=id,
    #     #                        recipe_id=recipe_id, form=form)
    #
    #     if form.validate_on_submit():
    #     # if current_user.is_authenticated:
    #         # username = User.query.get("username")
    #         # id = User.query.filter_by(username=form2.username.data).first()
    #         # recipe_id = Recipe.query.filter_by(recipe_name=recipe_name).recipe_id().first()
    #         # recipe_id = Recipe.query.filter_by(recipe).recipe_id()
    #         # recipe_id = Recipe.query.get(recipe_name)
    #         # commentquery = Comment.insert().values({"comment": usercomment}, recipe_id=recipe_id, username=username)
    #         # commentquery = Comment.update().values(usercomment, recipe_id, username)
    #         comment_query = Comment(comment=user_comment, id=1)
    #         db.session.add(comment_query)
    #         db.session.commit()
    #         print("Comment", form.comment.data)
    #         return render_template('specific_recipe.html', comment=comment, user_comment=user_comment, comment_query=comment_query, id=id, form=form)
    #
    #     else:
    #         return redirect(url_for('user_account'), form=form)
# @login_required
# def post_comments(recipe_name):
#     form1 = CommentForm()
#     form2 = UserAccountForm()

# user_comment = form1.comment.data
# id = User.query.filter_by(username=form2.username.data).first()
# recipe_id = Recipe.query.filter_by(recipe_name=recipe_name).recipe_id()

# if form1.validate_on_submit():
# comment_query = Comment(comment=user_comment, id=id, recipe_id=recipe_id)
# db.session.add(comment_query)
# db.session.commit()
# flash("Your comment has been posted")
# # return redirect(url_for('/recipes/<recipe_name>'))
# return render_template('specific_recipe.html', form1=form1, form2=form2, comment=user_comment, user_id=id, recipe_id=recipe_id )

@app.route("/recipes", methods=["GET", "POST"])
def recipe():
    recipes = Recipe.query.all()
    return render_template('recipe.html', recipes=recipes)


@app.route("/about", methods=["GET"])
def about():
    url = url_for('home')
    return render_template('about.html', title='about', page_title=url)


@app.route("/zero_waste", methods=["GET"])
def ZeroWaste():
    return render_template('zero_waste.html')


@app.route("/sustainability", methods=["GET"])
def sustainability():
    return render_template('sustainability.html')


@app.route("/food_banks", methods=["GET"])
def FoodBanks():
    return render_template('food_banks.html')


@app.route("/blog", methods=["GET", "POST"])
def blog():
    return render_template('blog.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserAccountForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created. You can log in using your email and password", "success")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('user_account'))
        else:
            flash('Login unsuccessful. Please check email and password')
    return render_template('login.html', title='Login', form=form)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pictures', picture_fn)

    output_size = (200, 200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/useraccount", methods=['GET', 'POST'])
@login_required
def user_account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('your account has been updated!', 'success')
        return redirect(url_for('user_account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
    return render_template('useraccount.html', title='Account', image_file=image_file, form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template('contact.html')

# # PREVIOUS CODE BEFORE CHARLOTTE COMMIT IS COMMENTED BELOW
# @app.route("/account", methods=["GET", "POST"])
# def account():
#     error = ""
#     form = UserAccountForm()
#
#     if request.method == 'POST':
#         first_name = form.first_name.data
#         last_name = form.last_name.data
#         username = form.username.data
#         email = form.email.data
#         password = form.password.data
#
#         if len(first_name) == 0 or len(last_name) == 0 or len(username) == 0 or len(email) == 0 or len(password) == 0:
#             error = "Please supply requested contact information"
#         else:
#             person = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
#             db.session.add(person)
#             db.session.commit()
#             return 'Thank you!'
#
#     return render_template('register.html', title="Register", form=form, message=error)
#
#
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     error = ""
#     form = UserLoginForm()
#
#     if request.method == 'POST':
#         email = form.email.data
#         password = form.password.data
#
#         if len(email) == 0 or len(password) == 0:
#             error = "Please supply requested log in details"
#         #   password validation needed here!
#         #   filter user table by password to allow user to log in
#         else:
#             # link to user's account page
#             return 'Access granted!'
#
#     return render_template('login.html', title="Register", form=form, message=error)
