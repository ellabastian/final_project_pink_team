from application import db


class Difficulty(db.Model):
    difficulty_id = db.Column(db.Integer, primary_key=True)
    difficulty_name = db.Column(db.String(50), nullable=False)
    recipes = db.relationship('Recipe', backref='difficulty')


class Recipe(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100), nullable=False)
    recipe_img = db.Column(db.String(500), nullable=True)
    recipe_difficulty = db.Column(db.Integer, db.ForeignKey('difficulty.difficulty_id'), nullable=False)
    recipe_prep_time = db.Column(db.String(50), nullable=False)
    recipe_cook_time = db.Column(db.String(50), nullable=False)
    recipe_category = db.Column(db.String(50), nullable=False)
    recipe_description = db.Column(db.String(500), nullable=False)
    instructions = db.relationship('Instruction', backref='recipe')
    ingredient_recipes = db.relationship('IngredientRecipe', backref='recipe')


class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(100), nullable=False)
    ingredient_recipes = db.relationship('IngredientRecipe', backref='ingredient')


class Instruction(db.Model):
    instruction_id = db.Column(db.Integer, primary_key=True)
    instruction_number = db.Column(db.Integer, nullable=False)
    instruction_description = db.Column(db.String(1000), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), nullable=False)


class IngredientRecipe(db.Model):
    ingredient_recipe_id = db.Column(db.Integer, primary_key=True)
    ingredient_recipe_measurement = db.Column(db.String(50), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.ingredient_id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), nullable=False)