from application import db
from application.models import Recipe, Ingredient, IngredientRecipe, Instruction, Difficulty

db.drop_all()
db.create_all()

easy = Difficulty(difficulty_name='Easy')
medium = Difficulty(difficulty_name='Medium')
hard = Difficulty(difficulty_name='Hard')

difficulty_list = [easy, medium, hard]
db.session.add_all(difficulty_list)

breakfast_burrito = Recipe(recipe_name='Breakfast Burrito', recipe_img="https://images.immediate.co.uk/production/volatile/sites/30/2020/08/breakfast-burrito-b086548.jpg?quality=90&webp=true&resize=300,272", recipe_difficulty=1, recipe_prep_time="5 minutes", recipe_cook_time="10 minutes", recipe_category="Breakfast", recipe_description="Make a nutritious cocoon for breakfast ingredients with a wholemeal wrap. We’ve included protein-rich eggs and avocado to add good fats to this burrito.")
courgette_lasagne = Recipe(recipe_name='Courgette Lasagne', recipe_img="https://images.immediate.co.uk/production/volatile/sites/30/2022/03/Creamy-courgette-lasagne-e63aa0c.jpg?quality=90&webp=true&resize=300,272", recipe_difficulty=1, recipe_prep_time="10 minutes", recipe_cook_time="20 minutes", recipe_category="Lunch", recipe_description="Serve this quick, creamy courgette & ricotta lasagne for a last-minute dinner party to impress vegetarian friends. It's a great way to use courgettes when they're in season.")
chilli_con_carne = Recipe(recipe_name='Chilli Con Carne', recipe_img="http://www.errenskitchen.com/wp-content/uploads/2017/02/Chilli-Con-Carne2.jpg", recipe_difficulty=2, recipe_prep_time="10 minutes", recipe_cook_time="1 hour", recipe_category="Dinner", recipe_description="Make classic chilli con carne tonight for spicy comfort food, or try different options with beans, veggies or turkey mince. Serve with tortillas.")

db.session.add(breakfast_burrito)
db.session.add(courgette_lasagne)
db.session.add(chilli_con_carne)

breakfast_burrito_step_one = Instruction(instruction_number=1, instruction_description="In a large baking dish, layer up the lasagne, starting with half the courgette mix, then pasta, then tomato sauce. Repeat, top with blobs of the remaining ricotta, then scatter with the rest of the cheddar. Bake on the top shelf for about 10 mins until the pasta is tender and the cheese is golden.", recipe_id=1)
breakfast_burrito_step_two = Instruction(instruction_number=2, instruction_description="Whisk the chipotle paste with the egg and some seasoning in a jug. Heat the oil in a large frying pan, add the kale and tomatoes.", recipe_id=1)
breakfast_burrito_step_three = Instruction(instruction_number=3, instruction_description="Cook until the kale is wilted and the tomatoes have softened, then push everything to the side of the pan. Pour the beaten egg into the cleared half of the pan and scramble. Layer everything into the centre of your wrap, topping with the avocado, then wrap up and eat immediately.", recipe_id=1)

burrito_step_list = [breakfast_burrito_step_one, breakfast_burrito_step_two, breakfast_burrito_step_three]
db.session.add_all(burrito_step_list)

onion = Ingredient(ingredient_name='Onion')
red_pepper = Ingredient(ingredient_name='Red Pepper')
garlic = Ingredient(ingredient_name='Garlic Cloves')
oil = Ingredient(ingredient_name='Oil')
hot_chilli_pepper = Ingredient(ingredient_name='Hot Chilli Pepper')
paprika = Ingredient(ingredient_name='Paprika')
ground_cumin = Ingredient(ingredient_name='Ground Cumin')
lean_minced_beef = Ingredient(ingredient_name='Lean minced beef')
beef_stock_cube = Ingredient(ingredient_name='Beef Stock Cube')
canned_tomatoes = Ingredient(ingredient_name='Canned Chopped Tomatoes')
dried_marjoram = Ingredient(ingredient_name='Dried Marjoram')
sugar = Ingredient(ingredient_name='Sugar')
dark_chocolate = Ingredient(ingredient_name='Dark Chocolate')
tomato_puree = Ingredient(ingredient_name='Tomato Purée')
canned_kidney_beans = Ingredient(ingredient_name='Canned Red Kidney Beans')
long_grain_rice = Ingredient(ingredient_name='Long Grain Rice')
soured_cream = Ingredient(ingredient_name='Soured Cream')
lasagne_sheet = Ingredient(ingredient_name='Dried Lasagne Sheets')
sunflower_oil = Ingredient(ingredient_name='Sunflower Oil')
pasta_sauce = Ingredient(ingredient_name='Tomato sauce For Pasta Jar')
courgette = Ingredient(ingredient_name='Courgette')
ricotta = Ingredient(ingredient_name='Ricotta')
cheddar = Ingredient(ingredient_name='Cheddar')
chipotle_paste = Ingredient(ingredient_name='Chipotle Paste')
egg = Ingredient(ingredient_name='Egg')
rapeseed_oil = Ingredient(ingredient_name='Rapeseed Oil')
kale = Ingredient(ingredient_name='Kale')
cherry_tomato = Ingredient(ingredient_name='Cherry Tomato')
avocado = Ingredient(ingredient_name='Avocado')
wholemeal_tortilla_wrap = Ingredient(ingredient_name='Wholemeal Tortilla Wrap')

ingredients_list = [onion, red_pepper, garlic, oil, hot_chilli_pepper, paprika,
ground_cumin, lean_minced_beef, beef_stock_cube, canned_tomatoes, dried_marjoram, sugar,dark_chocolate,tomato_puree, canned_kidney_beans, long_grain_rice, soured_cream, lasagne_sheet,
sunflower_oil, pasta_sauce, courgette, ricotta, cheddar, chipotle_paste, egg, rapeseed_oil,kale,cherry_tomato,avocado, wholemeal_tortilla_wrap]

db.session.add_all(ingredients_list)

ingredients_in_recipe_1 = IngredientRecipe(ingredient_recipe_measurement="1 large", ingredient_id=1, recipe_id=3)
ingredients_in_recipe_2 = IngredientRecipe(ingredient_recipe_measurement="1", ingredient_id=2, recipe_id=3)
ingredients_in_recipe_3 = IngredientRecipe(ingredient_recipe_measurement="2 cloves", ingredient_id=3, recipe_id=3)
ingredients_in_recipe_4 = IngredientRecipe(ingredient_recipe_measurement="1 tbsp", ingredient_id=4, recipe_id=3)
ingredients_in_recipe_5 = IngredientRecipe(ingredient_recipe_measurement="1 heaped tsp", ingredient_id=5, recipe_id=3)
ingredients_in_recipe_6 = IngredientRecipe(ingredient_recipe_measurement="1 tsp", ingredient_id=6, recipe_id=3)
ingredients_in_recipe_7 = IngredientRecipe(ingredient_recipe_measurement="1 tsp", ingredient_id=7, recipe_id=3)
ingredients_in_recipe_8 = IngredientRecipe(ingredient_recipe_measurement="500g", ingredient_id=8, recipe_id=3)
ingredients_in_recipe_9 = IngredientRecipe(ingredient_recipe_measurement="1", ingredient_id=9, recipe_id=3)
ingredients_in_recipe_10 = IngredientRecipe(ingredient_recipe_measurement="400g can", ingredient_id=10, recipe_id=3)
ingredients_in_recipe_11 = IngredientRecipe(ingredient_recipe_measurement="0.5 tsp", ingredient_id=11, recipe_id=3)
ingredients_in_recipe_12 = IngredientRecipe(ingredient_recipe_measurement="1sp", ingredient_id=12, recipe_id=3)
ingredients_in_recipe_13 = IngredientRecipe(ingredient_recipe_measurement="thumb-sized piece", ingredient_id=13, recipe_id=3)
ingredients_in_recipe_14 = IngredientRecipe(ingredient_recipe_measurement="2 tbsp", ingredient_id=14, recipe_id=3)
ingredients_in_recipe_15 = IngredientRecipe(ingredient_recipe_measurement="410g can", ingredient_id=15, recipe_id=3)
ingredients_in_recipe_16 = IngredientRecipe(ingredient_recipe_measurement="plain boiled to serve", ingredient_id=16, recipe_id=3)
ingredients_in_recipe_17 = IngredientRecipe(ingredient_recipe_measurement="to serve", ingredient_id=17, recipe_id=3)
ingredients_in_recipe_18 = IngredientRecipe(ingredient_recipe_measurement="9 dried", ingredient_id=18, recipe_id=2)
ingredients_in_recipe_19 = IngredientRecipe(ingredient_recipe_measurement="1 tbsp", ingredient_id=19, recipe_id=2)
ingredients_in_recipe_20 = IngredientRecipe(ingredient_recipe_measurement="1", ingredient_id=20, recipe_id=2)
ingredients_in_recipe_21 = IngredientRecipe(ingredient_recipe_measurement="700g (about 6)", ingredient_id=21, recipe_id=2)
ingredients_in_recipe_22 = IngredientRecipe(ingredient_recipe_measurement="2 crushed", ingredient_id=22, recipe_id=2)
ingredients_in_recipe_23 = IngredientRecipe(ingredient_recipe_measurement="250g tub", ingredient_id=23, recipe_id=2)
ingredients_in_recipe_24 = IngredientRecipe(ingredient_recipe_measurement="50g", ingredient_id=24, recipe_id=2)
ingredients_in_recipe_25 = IngredientRecipe(ingredient_recipe_measurement="350g jar", ingredient_id=25, recipe_id=2)
ingredients_in_recipe_26 = IngredientRecipe(ingredient_recipe_measurement="1", ingredient_id=26, recipe_id=1)
ingredients_in_recipe_27 = IngredientRecipe(ingredient_recipe_measurement="1 tsp", ingredient_id=27, recipe_id=1)
ingredients_in_recipe_28 = IngredientRecipe(ingredient_recipe_measurement="50g", ingredient_id=28, recipe_id=1)
ingredients_in_recipe_29 = IngredientRecipe(ingredient_recipe_measurement="7 halved", ingredient_id=29, recipe_id=1)
ingredients_in_recipe_30 = IngredientRecipe(ingredient_recipe_measurement="Half a small", ingredient_id=30, recipe_id=1)

ingredients_in_recipe_list = [ingredients_in_recipe_1, ingredients_in_recipe_2, ingredients_in_recipe_3, ingredients_in_recipe_4, ingredients_in_recipe_5, ingredients_in_recipe_6, ingredients_in_recipe_7,
                              ingredients_in_recipe_8, ingredients_in_recipe_9, ingredients_in_recipe_10, ingredients_in_recipe_11, ingredients_in_recipe_12,
                              ingredients_in_recipe_13, ingredients_in_recipe_14, ingredients_in_recipe_15, ingredients_in_recipe_16, ingredients_in_recipe_17,
                              ingredients_in_recipe_18, ingredients_in_recipe_19, ingredients_in_recipe_20, ingredients_in_recipe_21, ingredients_in_recipe_22, ingredients_in_recipe_23, ingredients_in_recipe_24,
                              ingredients_in_recipe_25, ingredients_in_recipe_26, ingredients_in_recipe_27, ingredients_in_recipe_28, ingredients_in_recipe_29, ingredients_in_recipe_30]

db.session.add_all(ingredients_in_recipe_list)


db.session.commit()