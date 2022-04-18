from flask import render_template, request
from application import app
from application.ingredient_search import IngredientsForm

@app.route("/home", methods=["GET","POST"])
@app.route("/", methods=["GET","POST"])
def home():
    error = ""
    form = IngredientsForm()
    if request.method == "POST":
        ingredient_result = form.ingredients.data
        if len(ingredient_result) == 0:
            error = "Please supply an ingredient"
        else:
            return ingredient_result
    return render_template('home.html', form=form, message=error)