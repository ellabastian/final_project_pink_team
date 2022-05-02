from application import db, login_manager
from flask_login import UserMixin


class Comment(UserMixin, db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), nullable=False)
    time_created = db.Column(db.DateTime, nullable=False)


class Rating(UserMixin, db.Model):
    rating_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=True)
    id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), nullable=False)


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
    recipe_rating = db.Column(db.Integer, nullable=True)
    instructions = db.relationship('Instruction', backref='recipe')
    ingredient_recipes = db.relationship('IngredientRecipe', backref='recipe')
    comments = db.relationship('Comment', backref='recipe')
    ratings = db.relationship('Rating', backref='recipe')
    saved_recipes = db.relationship('SavedRecipe', backref='recipe')


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


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default='defaultprofilepic.png')
    comments = db.relationship('Comment', backref='user')
    ratings = db.relationship('Rating', backref='user')
    saved_recipes = db.relationship('SavedRecipe', backref='user')


class SavedRecipe(db.Model):
    saved_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), nullable=False)


