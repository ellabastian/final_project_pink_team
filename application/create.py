from application import db
from application.models import Recipe, Ingredient, IngredientRecipe, Instruction, Difficulty


db.create_all()
# db.drop_all()

# db.session.commit()