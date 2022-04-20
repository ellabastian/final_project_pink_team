from flask import render_template, request, url_for
from application import app, db
from application.ingredient_search import IngredientsForm
from application.models import Ingredient, IngredientRecipe, Recipe, Instruction, Difficulty


@app.route("/home", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():
    error = ""
    form = IngredientsForm()

    if request.method == "POST":
        ingredient_result = form.ingredients.data

        if len(ingredient_result) == 0:
            error = "Please supply an ingredient"
        else:
            # return ingredient_result
            stuff = Ingredient.query.all()
            # stuff = Ingredient.query.filter_by(ingredient_name=ingredient_result)
            return str(stuff)

            # trialling out queries below
            # query_result = db.execute("SELECT ingredient_name FROM ingredient WHERE ingredient_name = :ingredient_result", {"ingredient_result": ingredient_result})
            # return query_result
            # Ingredient.query.filter_by(ingredient_name=ingredient_result).first()
            # ingredient_id = Ingredient.query.get(ingredient_name)
            # query = Ingredient.query.get(ingredient_id)
            # return query

    return render_template('home.html', form=form, message=error)


@app.route("/recipe", methods=["GET", "POST"])
def recipe():
    return render_template('recipe.html')


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


@app.route("/account", methods=["GET", "POST"])
def account():
    return render_template('account.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template('contact.html')

