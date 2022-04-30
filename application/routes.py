import os
import secrets
from PIL import Image
from flask import render_template, request, url_for, redirect, flash, get_flashed_messages, session
from application import app, db, bcrypt
from application.forms import IngredientsForm, UserAccountForm, UserLoginForm, UpdateAccountForm, \
    UserFeedback, DeleteUserFeedback, SaveRecipe, ViewRecipes
from application.models import Ingredient, IngredientRecipe, Recipe, Instruction, Difficulty, User, Comment, SavedRecipe
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime


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
    recipe = (Recipe.query.filter_by(recipe_name=recipe_name).first())
    instructions = Instruction.query.filter_by(recipe_id=recipe.recipe_id).all()
    list_of_comments = Comment.query.filter_by(recipe_id=recipe.recipe_id).all()
    form = UserFeedback()
    save_form = SaveRecipe(user_id=current_user.id, recipe_id=recipe.recipe_id)
    list_of_usernames = []
    for comment in list_of_comments:
        username = User.query.filter_by(id=comment.user_id).first().username
        list_of_usernames.append(username)

    if form.validate_on_submit():

        if current_user.is_authenticated:
            comment_query = Comment(comment=form.comment.data, user_id=current_user.id, recipe_id=recipe.recipe_id, time_created=datetime.now())
            db.session.add(comment_query)
            db.session.commit()

            return render_template('specific_recipe.html', recipe_name=recipe_name, comment_query=comment_query,
                                   form=form, list_of_comments=list_of_comments, recipe=recipe,
                                   list_of_usernames=list_of_usernames, save_form=save_form, instructions=instructions)

        else:
            return redirect(url_for('register'))

    return render_template('specific_recipe.html', recipe_name=recipe_name, recipe=recipe, form=form,
                           save_form=save_form, user=current_user, list_of_comments=list_of_comments,
                           list_of_usernames=list_of_usernames, instructions=instructions)


@app.route("/save-recipe", methods=["POST"])
def save_recipe():
    db.session.add(SavedRecipe(user_id=request.form['user_id'], recipe_id=request.form['recipe_id']))
    db.session.commit()
    return redirect(url_for('saved'))
            

@app.route("/delete/<int:comment_id>", methods=["GET", "POST", "DELETE"])
def delete(comment_id):
    comment = Comment.query.get(comment_id)
    form = DeleteUserFeedback()
    if comment:
        if form.validate_on_submit():
            db.session.delete(comment)
            db.session.commit()
            flash("Comment deleted")
            return redirect(url_for('recipe'))
        return render_template('delete.html', form=form, comment=comment, comment_id=comment_id)
    else:
        flash("Comment not found")
        return redirect(url_for('recipe'))


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
    view_recipe_form = ViewRecipes()

    user = User.query.filter_by(id=current_user.id).first()
    saved_ids = (SavedRecipe.query.filter_by(user_id=user.id).all())
    saved_recipes = []
    for saved_id in saved_ids:
        recipe_id = saved_id.recipe_id
        saved_recipes.extend(Recipe.query.filter_by(recipe_id=recipe_id).all())


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
    return render_template('useraccount.html', title='Account', image_file=image_file, form=form, user=user,
                           saved_recipes=saved_recipes, saved_ids=saved_ids, view_recipe_form=view_recipe_form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template('contact.html')


@app.route("/saved-recipes", methods=["GET", "POST"])
def saved():
    user = User.query.filter_by(username=current_user.username).first()
    saved_ids = (SavedRecipe.query.filter_by(user_id=user.id).all())
    saved_recipes = []
    for saved_id in saved_ids:
        recipe_id = saved_id.recipe_id
        saved_recipes.extend(Recipe.query.filter_by(recipe_id=recipe_id).all())
    return render_template('saved_recipe.html', user=user, saved_recipes=saved_recipes)


