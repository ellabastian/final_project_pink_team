import os
import secrets
from PIL import Image
from flask import render_template, request, url_for, redirect, flash, get_flashed_messages, session
from application import app, db, bcrypt
from application.forms import IngredientsForm, UserAccountForm, UserLoginForm, UpdateAccountForm, UserFeedback, DeleteUserFeedback, SaveRecipe, ViewRecipes
from application.models import Ingredient, IngredientRecipe, Recipe, Instruction, Difficulty, User, Comment, SavedRecipe, Rating
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from sqlalchemy.sql import func


# HOMEPAGE
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

    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
        return render_template('home.html', form=form, message=error, image_file=image_file)

    else:
        return render_template('no_user_home.html', form=form, message=error)


# ALL RECIPES PAGE
@app.route("/recipes", methods=["GET", "POST"])
def recipe():
    recipes = Recipe.query.all()
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
        return render_template('recipe.html', recipes=recipes, image_file=image_file)
    else:
        return render_template('recipe.html', recipes=recipes)


# DYNAMIC SPECIFIC RECIPE PAGE
@app.route("/recipes/<recipe_name>", methods=["GET", "POST"])
def specific_recipe(recipe_name):
    recipe = (Recipe.query.filter_by(recipe_name=recipe_name).first())
    instructions = Instruction.query.filter_by(recipe_id=recipe.recipe_id).all()
    comments = db.session.query(Recipe, Comment, User).filter(Recipe.recipe_id == Comment.recipe_id).\
        filter(Comment.user_id == User.id).filter(Recipe.recipe_id == recipe.recipe_id).all()
    if current_user.is_authenticated:
        save_form = SaveRecipe(user_id=current_user.id, recipe_id=recipe.recipe_id)
        image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
        form = UserFeedback(user_id=current_user.id, recipe_id=recipe.recipe_id)
        return render_template('specific_recipe.html', recipe_name=recipe_name, recipe=recipe, form=form,
                           save_form=save_form, user=current_user, instructions=instructions , image_file=image_file,
                               comments=comments)
    else:
       return render_template('no_user_specific_recipe.html', recipe_name=recipe_name, recipe=recipe, user=current_user,
                              instructions=instructions, comments=comments)



# INTERNAL PAGE - FORM TO SAVE RECIPE TO USER ACCOUNT
@app.route("/save_recipe", methods=["POST"])
def save_recipe():
    db.session.add(SavedRecipe(user_id=request.form['user_id'], recipe_id=request.form['recipe_id']))
    db.session.commit()
    flash("Recipe saved!")
    return redirect(url_for('saved'))


@app.route("/user_feedback", methods=["POST"])
def user_feedback():
    rating_query = Rating(rating=request.form['recipe_rating'], id=request.form['user_id'],
                          recipe_id=request.form['recipe_id'])
    comment_query = Comment(comment=request.form['comment'], user_id=request.form['user_id'],
                          recipe_id=request.form['recipe_id'], time_created=datetime.now())
    db.session.add(comment_query)
    db.session.add(rating_query)
    average = Rating.query.with_entities(func.avg(Rating.rating)) \
            .filter_by(recipe_id=request.form['recipe_id']).first()
    Recipe.query.filter_by(recipe_id=request.form['recipe_id']).update({"recipe_rating":average[0]})
    db.session.commit()
    recipe_name = Recipe.query.filter_by(recipe_id=request.form['recipe_id']).first().recipe_name
    flash("Comment submitted!")
    return redirect(url_for('specific_recipe', recipe_name=recipe_name))


# INTERNAL PAGE - FORM TO DELETE COMMENT FROM RECIPE PAGE 
@app.route("/delete/<int:comment_id>", methods=["GET", "POST", "DELETE"])
def delete(comment_id):
    comment = Comment.query.get(comment_id)
    get_recipe_id = Comment.query.filter_by(comment_id=comment_id).first().recipe_id
    recipe_name = Recipe.query.filter_by(recipe_id=get_recipe_id).first().recipe_name
    image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
    form = DeleteUserFeedback()
    if comment:
        if form.validate_on_submit():
            db.session.delete(comment)
            db.session.commit()
            flash("Comment deleted")
            return redirect(url_for('specific_recipe', recipe_name=recipe_name))
        return render_template('delete.html', form=form, comment=comment, comment_id=comment_id,
                               recipe_name=recipe_name, image_file=image_file)
    else:
        flash("Comment not found")
        return redirect(url_for('recipe'))


# ABOUT US PAGE  
@app.route("/about", methods=["GET"])
def about():
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
        return render_template('about.html', image_file=image_file)
    else:
        return render_template('about.html')


# ZERO WASTE PAGE  
@app.route("/zero_waste", methods=["GET"])
def ZeroWaste():
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
        return render_template('zero_waste.html', image_file=image_file)
    else:
        return render_template('zero_waste.html')


# SUSTAINABILITY PAGE  
@app.route("/sustainability", methods=["GET"])
def sustainability():
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
        return render_template('sustainability.html', image_file=image_file)
    else:
        return render_template('sustainability.html')


# FOOD BANKS PAGE  
@app.route("/food_banks", methods=["GET"])
def FoodBanks():
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
        return render_template('food_banks.html', image_file=image_file)
    else:
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


# LOGIN TO ACCOUNT PAGE  
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


# USER ACCOUNT PAGE  
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


# INTERNAL PAGE - USER LOGOUT  
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


# CONTACT US PAGE  
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
        return render_template('contact.html', image_file=image_file)
    else:
        return render_template('contact.html')


@app.route("/saved-recipes", methods=["GET", "POST"])
def saved():
    user = User.query.filter_by(username=current_user.username).first()
    saved_ids = (SavedRecipe.query.filter_by(user_id=user.id).all())
    saved_recipes = []
    for saved_id in saved_ids:
        recipe_id = saved_id.recipe_id
        saved_recipes.extend(Recipe.query.filter_by(recipe_id=recipe_id).all())
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
        return render_template('saved_recipe.html', user=user, saved_recipes=saved_recipes, image_file=image_file)
    else:
        return render_template('saved_recipe.html', user=user, saved_recipes=saved_recipes)

