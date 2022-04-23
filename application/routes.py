from flask import render_template, request, url_for, redirect, flash
from application import app, db, bcrypt
from application.forms import IngredientsForm, UserAccountForm, UserLoginForm
from application.models import Ingredient, IngredientRecipe, Recipe, Instruction, Difficulty, User
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


@app.route("/recipes/<recipe_name>")
def specific_recipe(recipe_name):
    recipe = (Recipe.query.filter_by(recipe_name=recipe_name).first())
    instructions = Instruction.query.filter_by(recipe_id=recipe.recipe_id).all()
    return render_template('specific_recipe.html', recipe_name=recipe_name, recipe=recipe, instructions=instructions)


@app.route("/recipes", methods=["GET", "POST"])
def recipe():
    recipes = Recipe.query.all()
    return render_template('recipe.html', recipes=recipes)


@app.route("/about", methods=["GET"])
def about():
    url = url_for('home')
    return render_template('about.html', title='about', page_title=url)


@app.route("/resources", methods=["GET"])
def resources():
    return render_template('resources.html')


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
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data, email=form.email.data, password=hashed_password)
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


@app.route("/useraccount")
@login_required
def user_account():
    return render_template('useraccount.html', title='Account')


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