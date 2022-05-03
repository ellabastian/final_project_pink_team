from application import db
from application.models import Recipe, Ingredient, IngredientRecipe, Instruction, Difficulty, User, Comment, Rating, SavedRecipe
from datetime import datetime

db.drop_all()
db.create_all()
#
# Inserting Values into the Difficulty table
easy = Difficulty(difficulty_name='Easy')
medium = Difficulty(difficulty_name='Medium')
hard = Difficulty(difficulty_name='Hard')

difficulty_list = [easy, medium, hard]
db.session.add_all(difficulty_list)

# Inserting values into the Recipe table
# recipe_template = Recipe(recipe_name="", recipe_img="", recipe_difficulty=, recipe_prep_time="", recipe_cook_time="", recipe_category="", recipe_description="")
breakfast_burrito = Recipe(recipe_name="Breakfast Burrito",
                           recipe_img="https://images.immediate.co.uk/production/volatile/sites/30/2020/08/breakfast-burrito-b086548.jpg?quality=90&webp=true&resize=300,272",
                           recipe_difficulty=1, recipe_prep_time="5 minutes", recipe_cook_time="10 minutes", recipe_category="Breakfast",
                           recipe_description="Make a nutritious cocoon for breakfast ingredients with a wholemeal wrap. We’ve included protein-rich eggs and avocado to add good fats to this burrito.", recipe_rating=1)
courgette_lasagne = Recipe(recipe_name="Courgette Lasagne",
                           recipe_img="https://images.immediate.co.uk/production/volatile/sites/30/2022/03/Creamy-courgette-lasagne-e63aa0c.jpg?quality=90&webp=true&resize=300,272",
                           recipe_difficulty=1, recipe_prep_time="10 minutes", recipe_cook_time="20 minutes", recipe_category="Lunch",
                           recipe_description="Serve this quick, creamy courgette & ricotta lasagne for a last-minute dinner party to impress vegetarian friends. It's a great way to use courgettes when they're in season.", recipe_rating=1)
chilli_con_carne = Recipe(recipe_name="Chilli Con Carne", recipe_img="http://www.errenskitchen.com/wp-content/uploads/2017/02/Chilli-Con-Carne2.jpg", recipe_difficulty=2, recipe_prep_time="10 minutes", recipe_cook_time="1 hour", recipe_category="Dinner", recipe_description="Make classic chilli con carne tonight for spicy comfort food, or try different options with beans, veggies or turkey mince. Serve with tortillas.", recipe_rating=3)
orange_almond_vegan_cake = Recipe(recipe_name="Orange Almond Vegan Cake", recipe_img="https://i.pinimg.com/originals/50/18/f9/5018f9d32382b19a54fbc3d20ac19076.jpg", recipe_difficulty=1, recipe_prep_time="20 minutes", recipe_cook_time="1 hour", recipe_category="Dessert", recipe_description="Make this no fuss vegan cake. Perfect for any day and for sharing with the people you love and hate.", recipe_rating=4)
vegan_apple_tarts = Recipe(recipe_name="Vegan Apple Tarts", recipe_img="https://www.jusrol.co.uk/wp-content/uploads/2018/08/168_Image_Hero-Image_2018_7_6_19_38_17.jpg", recipe_difficulty=1, recipe_prep_time="15 minutes", recipe_cook_time="30 minutes", recipe_category="Breakfast", recipe_description="It is said that an apple a day keeps the doctor away, and this recipe will have you eating several apples every day, hopefully your doctor won't mind!", recipe_rating=5)
prawn_tikka_masala = Recipe(recipe_name="Prawn Tikka Masala", recipe_img="https://images.immediate.co.uk/production/volatile/sites/30/2020/08/prawn-tikka-masala-a4a86f9.jpg?quality=90&webp=true&resize=300,272", recipe_difficulty=1, recipe_prep_time="10 minutes", recipe_cook_time="30 minutes", recipe_category="Dinner", recipe_description="Forget a takeaway and tuck into a midweek meal that will please the whole family with our easy, low calorie prawn tikka masala. Serve with naan!")
jerk_chicken_with_rice_and_peas = Recipe(recipe_name="Jerk Chicken with Rice and Peas", recipe_img="https://images.immediate.co.uk/production/volatile/sites/30/2020/08/recipe-image-legacy-id-1047528_11-62a849b.jpg?quality=90&webp=true&resize=300,272", recipe_difficulty=2, recipe_prep_time="25 minutes", recipe_cook_time="40 minutes", recipe_category="Dinner", recipe_description="Jerk refers to a style of cooking in which the main ingredient—which most often is chicken but may also be beef, pork, goat, boar, seafood, or vegetables—is coated in spices and slow-cooked over a fire or grill traditionally composed of green pimento wood positioned over burning coals.")

# db.session.add()
db.session.add(breakfast_burrito)
db.session.add(courgette_lasagne)
db.session.add(chilli_con_carne)
db.session.add(orange_almond_vegan_cake)
db.session.add(vegan_apple_tarts)
db.session.add(prawn_tikka_masala)
db.session.add(jerk_chicken_with_rice_and_peas)

# Inserting values into the Instruction table
# template = Instruction(instruction_number=, instruction_description="", recipe_id=)


# Breakfast Burrito
breakfast_burrito_step_one = Instruction(instruction_number=1, instruction_description="Whisk the chipotle paste with the egg and some seasoning in a jug. Heat the oil in a large frying pan, add the kale and tomatoes.", recipe_id=1)
breakfast_burrito_step_two = Instruction(instruction_number=2, instruction_description="Cook until the kale is wilted and the tomatoes have softened, then push everything to the side of the pan. Pour the beaten egg into the cleared half of the pan and scramble.", recipe_id=1)
breakfast_burrito_step_three = Instruction(instruction_number=3, instruction_description="Layer everything into the centre of your wrap, topping with the avocado, then wrap up and eat immediately.", recipe_id=1)

burrito_step_list = [breakfast_burrito_step_one, breakfast_burrito_step_two, breakfast_burrito_step_three]
db.session.add_all(burrito_step_list)


# Courgette Lasagne
courgette_lasagne_step_one = Instruction(instruction_number=1, instruction_description="Heat oven to 220C/fan 200C/gas 7. Put a pan of water on to boil, then cook the lasagne sheets for about 5 mins until softened, but not cooked through. Rinse in cold water, then drizzle with a little oil to stop them sticking together.", recipe_id=2)
courgette_lasagne_step_two = Instruction(instruction_number=2, instruction_description="Meanwhile, heat the oil in a large frying pan, then fry the onion. After 3 mins, add the courgettes and garlic and continue to fry until the courgette has softened and turned bright green. Stir in 2/3 of both the ricotta and the cheddar, then season to taste. Heat the tomato sauce in the microwave for 2 mins on High until hot.", recipe_id=2)
courgette_lasagne_step_three = Instruction(instruction_number=3, instruction_description="In a large baking dish, layer up the lasagne, starting with half the courgette mix, then pasta, then tomato sauce. Repeat, top with blobs of the remaining ricotta, then scatter with the rest of the cheddar. Bake on the top shelf for about 10 mins until the pasta is tender and the cheese is golden.", recipe_id=2)

courgette_lasagne_step_list = [courgette_lasagne_step_one, courgette_lasagne_step_two, courgette_lasagne_step_three]
db.session.add_all(courgette_lasagne_step_list)


# Chilli Con Carne
chilli_con_carne_step_one = Instruction(instruction_number=1, instruction_description="Prepare your vegetables. Chop 1 large onion into small dice, about 5mm square. The easiest way to do this is to cut the onion in half from root to tip, peel it and slice each half into thick matchsticks lengthways, not quite cutting all the way to the root end so they are still held together. Slice across the matchsticks into neat dice.", recipe_id=3)
chilli_con_carne_step_two = Instruction(instruction_number=2, instruction_description="Cut 1 red pepper in half lengthways, remove stalk and wash the seeds away, then chop. Peel and finely chop 2 garlic cloves.", recipe_id=3)
chilli_con_carne_step_three = Instruction(instruction_number=3, instruction_description="Start cooking. Put your pan on the hob over a medium heat. Add 1 tbsp oil and leave it for 1-2 minutes until hot (a little longer for an electric hob).", recipe_id=3)
chilli_con_carne_step_four = Instruction(instruction_number=4, instruction_description="Add the onion and cook, stirring fairly frequently, for about 5 minutes, or until the onion is soft, squidgy and slightly translucent.", recipe_id=3)
chilli_con_carne_step_five = Instruction(instruction_number=5, instruction_description="Tip in the garlic, red pepper, 1 heaped tsp hot chilli powder or 1 level tbsp mild chilli powder, 1 tsp paprika and 1 tsp ground cumin.", recipe_id=3)
chilli_con_carne_step_six = Instruction(instruction_number=6, instruction_description="Give it a good stir, then leave it to cook for another 5 minutes, stirring occasionally.", recipe_id=3)
chilli_con_carne_step_seven = Instruction(instruction_number=7, instruction_description="Brown 500g lean minced beef. Turn the heat up a bit, add the meat to the pan and break it up with your spoon or spatula. The mix should sizzle a bit when you add the mince.", recipe_id=3)
chilli_con_carne_step_eight = Instruction(instruction_number=8, instruction_description="Keep stirring and prodding for at least 5 minutes, until all the mince is in uniform, mince-sized lumps and there are no more pink bits. Make sure you keep the heat hot enough for the meat to fry and become brown, rather than just stew.", recipe_id=3)
chilli_con_carne_step_nine = Instruction(instruction_number=9, instruction_description="Make the sauce. Crumble 1 beef stock cube into 300ml hot water. Pour this into the pan with the mince mixture.", recipe_id=3)
chilli_con_carne_step_ten = Instruction(instruction_number=10, instruction_description="Add a 400g can of chopped tomatoes. Tip in ½ tsp dried marjoram, 1 tsp sugar and add a good shake of salt and pepper. Squirt in about 2 tbsp tomato purée and stir the sauce well.", recipe_id=3)
chilli_con_carne_step_eleven = Instruction(instruction_number=11, instruction_description="Simmer it gently. Bring the whole thing to the boil, give it a good stir and put a lid on the pan. Turn down the heat until it is gently bubbling and leave it for 20 minutes.", recipe_id=3)
chilli_con_carne_step_twelve = Instruction(instruction_number=12, instruction_description="Check on the pan occasionally to stir it and make sure the sauce doesn’t catch on the bottom of the pan or isn’t drying out. If it is, add a couple of tablespoons of water and make sure that the heat really is low enough. After simmering gently, the saucy mince mixture should look thick, moist and juicy.", recipe_id=3)
chilli_con_carne_step_thirteen = Instruction(instruction_number=13, instruction_description="Drain and rinse a 410g can of red kidney beans in a sieve and stir them into the chilli pot. Bring to the boil again, and gently bubble without the lid for another 10 minutes, adding a little more water if it looks too dry.", recipe_id=3)
chilli_con_carne_step_fourteen = Instruction(instruction_number=14, instruction_description="Taste a bit of the chilli and season. It will probably take a lot more seasoning than you think.", recipe_id=3)
chilli_con_carne_step_fifteen = Instruction(instruction_number=15, instruction_description="Now replace the lid, turn off the heat and leave your chilli to stand for 10 minutes before serving. This is really important as it allows the flavours to mingle.", recipe_id=3)
chilli_con_carne_step_sixteen = Instruction(instruction_number=16, instruction_description="Serve with soured cream and plain boiled long grain rice.", recipe_id=3)

chilli_con_carne_step_list = [chilli_con_carne_step_one, chilli_con_carne_step_two, chilli_con_carne_step_three,
                              chilli_con_carne_step_four, chilli_con_carne_step_five, chilli_con_carne_step_six,
                              chilli_con_carne_step_seven, chilli_con_carne_step_eight, chilli_con_carne_step_nine,
                              chilli_con_carne_step_ten, chilli_con_carne_step_eleven, chilli_con_carne_step_twelve,
                              chilli_con_carne_step_thirteen, chilli_con_carne_step_fourteen,
                              chilli_con_carne_step_fifteen, chilli_con_carne_step_sixteen]
db.session.add_all(chilli_con_carne_step_list)


# Orange Almond Vegan Cake
orange_almond_vegan_cake_step_one = Instruction(instruction_number=1, instruction_description="Preheat the oven to 180C and grease and line a cake tin with baking paper.", recipe_id=4)
orange_almond_vegan_cake_step_two = Instruction(instruction_number=2, instruction_description="In a bowl combine rapeseed oil. sugar, almond milk and mix to combine. Pour in fresh orange juice then mix in orange zest.", recipe_id=4)
orange_almond_vegan_cake_step_three = Instruction(instruction_number=3, instruction_description="In a separate bowl, Sift in the plain flour, baking powder, bicarbonate of soda, ground almonds and a pinch of salt.", recipe_id=4)
orange_almond_vegan_cake_step_four = Instruction(instruction_number=4, instruction_description="Grease the cake tin and line the base with a disc of baking paper. Then, combine wet mixture with the dry gently until smooth.", recipe_id=4)
orange_almond_vegan_cake_step_five = Instruction(instruction_number=5, instruction_description="Quickly spoon the cake mix into the prepared tin, spread level with the back of a spoon and bake on the middle shelf of the preheated oven for 40 minutes to 1 hour.", recipe_id=4)
orange_almond_vegan_cake_step_six = Instruction(instruction_number=6, instruction_description="Leave the cake until completely cold before removing from the tin and serving.", recipe_id=4)

orange_almond_vegan_cake_step_list = [orange_almond_vegan_cake_step_one, orange_almond_vegan_cake_step_two,
                                      orange_almond_vegan_cake_step_three, orange_almond_vegan_cake_step_four,
                                      orange_almond_vegan_cake_step_five, orange_almond_vegan_cake_step_six]
db.session.add_all(orange_almond_vegan_cake_step_list)


# Vegan Apple Tarts
vegan_apple_tarts_step_one = Instruction(instruction_number=1, instruction_description="Divide puff pastry into 6 even squares. This is based on using Jus Rol puff pastry sheet. Puff pastry sheets may vary in size, the goal is to make easy medium sized squares.", recipe_id=5)
vegan_apple_tarts_step_two = Instruction(instruction_number=2, instruction_description="Mix 1 tbsp of maple syrup and 3 tbsp of plant-based milk together and brush the mixture across each side of each square.", recipe_id=5)
vegan_apple_tarts_step_three = Instruction(instruction_number=3, instruction_description="Add 1 tbsp of apple sauce in the centre of each puff pastry square.", recipe_id=5)
vegan_apple_tarts_step_four = Instruction(instruction_number=4, instruction_description="Place finely sliced apples in the centre of each puff pastry square on top of the apple sauce.", recipe_id=5)
vegan_apple_tarts_step_five = Instruction(instruction_number=5, instruction_description="Working with one pastry at a time, grab each corner of one side of the square and pinch each corner together covering half of the apples on one side of the pastry. Then repeat with the opposite side of the square puff pastry to then cover the other half of the apples.", recipe_id=5)
vegan_apple_tarts_step_six = Instruction(instruction_number=6, instruction_description="Place puff pastries in a preheated oven until golden brown.", recipe_id=5)
vegan_apple_tarts_step_seven = Instruction(instruction_number=7, instruction_description="Remove pastries from the oven and brush with maple syrup to get a nice glossy finish.", recipe_id=5)

vegan_apple_tarts_step_list = [vegan_apple_tarts_step_one, vegan_apple_tarts_step_two, vegan_apple_tarts_step_three,
                               vegan_apple_tarts_step_four, vegan_apple_tarts_step_five, vegan_apple_tarts_step_six,
                               vegan_apple_tarts_step_seven]
db.session.add_all(vegan_apple_tarts_step_list)


# Prawn Tikka Masala
prawn_tikka_masala_step_one = Instruction(instruction_number=1, instruction_description="Put the onion, ginger and garlic in a food processor and blitz to a smooth paste. ", recipe_id=6)
prawn_tikka_masala_step_two = Instruction(instruction_number=2, instruction_description="Heat the oil in a large flameproof casserole dish or pan over a medium heat. Add the onion paste and fry for 8 minutes or until lightly golden. ", recipe_id=6)
prawn_tikka_masala_step_three = Instruction(instruction_number=3, instruction_description="Stir in the curry paste and fry for 1 min more. Add the tomatoes, tomato purée, sugar and cardamom pods. Bring to a simmer and cook, covered, for another 10 minutes.", recipe_id=6)
prawn_tikka_masala_step_four = Instruction(instruction_number=4, instruction_description="Cook the rice following pack instructions.", recipe_id=6)
prawn_tikka_masala_step_five = Instruction(instruction_number=5, instruction_description="Scoop the cardamom out of the curry sauce and discard, then blitz with a hand blender, or in a clean food processor. Return to the pan, add the almonds and prawns, and cook for 5 minutes. Season to taste and stir through the cream and coriander. Optional: Serve with the rice and naan.", recipe_id=6)

prawn_tikka_masala_step_list = [prawn_tikka_masala_step_one, prawn_tikka_masala_step_two, prawn_tikka_masala_step_three,
                                prawn_tikka_masala_step_four, prawn_tikka_masala_step_five]
db.session.add_all(prawn_tikka_masala_step_list)

#jerk_chicken_with_rice_and_peas
jerk_chicken_with_rice_and_peas_step_one = Instruction(instruction_number=1,instruction_description="To make the jerk marinade, combine the spring onions, ginger, garlic, onion, scotch bonnet chillies, dried thyme, lime juice, soy sauce, vegetable oil, brown sugar and ground allspice in a food processor along with 1 tsp salt, and blend to a purée. If you’re having trouble getting it to blend, just keep turning off the blender, stirring the mixture, and trying again. Eventually it will start to blend up – don’t be tempted to add water, as you want a thick paste.", recipe_id= 7)
jerk_chicken_with_rice_and_peas_step_two = Instruction(instruction_number=2,instruction_description="Taste the jerk mixture for seasoning – it should taste pretty salty, but not unpleasantly, puckering salty. You can now throw in more chillies if it’s not spicy enough for you. If it tastes too salty and sour, try adding in a bit more brown sugar until the mixture tastes well balanced.", recipe_id= 7)
jerk_chicken_with_rice_and_peas_step_three = Instruction(instruction_number=3,instruction_description="Make a few slashes in 12 chicken thighs and pour the marinade over the meat, rubbing it into all the crevices. Cover and leave to marinate overnight in the fridge", recipe_id= 7)
jerk_chicken_with_rice_and_peas_step_four = Instruction(instruction_number=4,instruction_description="If you want to barbecue your chicken, get the coals burning 1 hr or so before you’re ready to cook. Authentic jerked meats are not exactly grilled as we think of grilling, but sort of smoke-grilled. To get a more authentic jerk experience, add some wood chips to your barbecue, and cook your chicken over slow, indirect heat for 30 mins.", recipe_id= 7)
jerk_chicken_with_rice_and_peas_step_five = Instruction(instruction_number=5,instruction_description="To cook in the oven, heat to 180C/160C fan/gas 4. Put the chicken pieces in a roasting tin with the halved lime and cook for 45 mins until tender and cooked through", recipe_id= 7)
jerk_chicken_with_rice_and_peas_step_six = Instruction(instruction_number=6,instruction_description="Season with salt, add 300ml cold water and set over a high heat. Once the rice begins to boil, turn it down to a medium heat, cover and cook for 10 mins. Add the kidney beans to the rice, then cover with a lid. Leave off the heat for 5 mins until all the liquid is absorbed.", recipe_id=7)
jerk_chicken_with_rice_and_peas_step_seven = Instruction(instruction_number=7,instruction_description="Squeeze the roasted lime over the chicken and serve with the rice & peas, and some hot sauce if you like it really spicy.", recipe_id=7)

jerk_chicken_with_rice_and_peas_step_list = [jerk_chicken_with_rice_and_peas_step_one, jerk_chicken_with_rice_and_peas_step_two, jerk_chicken_with_rice_and_peas_step_three, jerk_chicken_with_rice_and_peas_step_four,
                                             jerk_chicken_with_rice_and_peas_step_five, jerk_chicken_with_rice_and_peas_step_six, jerk_chicken_with_rice_and_peas_step_seven]
db.session.add_all(jerk_chicken_with_rice_and_peas_step_list)

# Inserting values into Ingredient table
onion = Ingredient(ingredient_name='Onion')
red_pepper = Ingredient(ingredient_name='Red Pepper')
garlic = Ingredient(ingredient_name='Garlic Cloves')
oil = Ingredient(ingredient_name='Oil')
hot_chilli_pepper = Ingredient(ingredient_name='Hot Chilli Pepper')
paprika = Ingredient(ingredient_name='Paprika')
ground_cumin = Ingredient(ingredient_name='Ground Cumin')
lean_minced_beef = Ingredient(ingredient_name='Lean minced beef')
beef_stock_cube = Ingredient(ingredient_name='Beef Stock Cube')
canned_tomatoes = Ingredient(ingredient_name='Chopped Tomatoes')
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
plain_flour = Ingredient(ingredient_name='Plain Flour')
ground_almonds = Ingredient(ingredient_name='Ground Almonds')
baking_soda = Ingredient(ingredient_name='Baking soda')
baking_powder = Ingredient(ingredient_name='Baking Powder')
salt = Ingredient(ingredient_name='Salt')
almond_milk = Ingredient(ingredient_name='Almond Milk')
caster_sugar = Ingredient(ingredient_name='Caster Sugar')
orange = Ingredient(ingredient_name='Orange')
vinegar = Ingredient(ingredient_name='Vinegar')
puff_pastry_sheet = Ingredient(ingredient_name='Puff Pastry Sheet')
apple_sauce = Ingredient(ingredient_name='Apple Sauce')
apple = Ingredient(ingredient_name='Apple')
maple_syrup = Ingredient(ingredient_name='Maple Syrup')
plant_based_milk = Ingredient(ingredient_name='Plant-based Milk')
ginger = Ingredient(ingredient_name='Ginger')
tikka_curry_paste = Ingredient(ingredient_name='Tikka Curry Paste')
light_brown_soft_sugar = Ingredient(ingredient_name='Light Brown Soft Sugar')
cardamom_pods = Ingredient(ingredient_name='Cardamom Pods')
brown_basmati_rice = Ingredient(ingredient_name='Brown Basmati Rice')
raw_king_prawns = Ingredient(ingredient_name='Raw King Prawns')
double_cream = Ingredient(ingredient_name='Double cream')
coriander = Ingredient(ingredient_name='Coriander')
naan = Ingredient(ingredient_name='Naan')
chicken_thighs = Ingredient(ingredient_name='Chicken Thighs')
lime = Ingredient(ingredient_name='Lime')
spring_onions = Ingredient(ingredient_name='Spring Onions')
scotch_bonnet_chillies = Ingredient(ingredient_name='Scotch Bonnet Chillies')
thyme = Ingredient(ingredient_name='Thyme')
soy_sauce = Ingredient(ingredient_name='Soy Sauce')
vegetable_oil = Ingredient(ingredient_name='Vegetable Oil')
allspice = Ingredient(ingredient_name='Allspice')
white_basmati_rice = Ingredient(ingredient_name='White Basmati Rice')
coconut_milk = Ingredient(ingredient_name='Coconut Milk')

ingredients_list = [onion, red_pepper, garlic, oil, hot_chilli_pepper, paprika, ground_cumin, lean_minced_beef,
                    beef_stock_cube, canned_tomatoes, dried_marjoram, sugar, dark_chocolate, tomato_puree,
                    canned_kidney_beans, long_grain_rice, soured_cream, lasagne_sheet, sunflower_oil, pasta_sauce,
                    courgette, ricotta, cheddar, chipotle_paste, egg, rapeseed_oil, kale, cherry_tomato, avocado,
                    wholemeal_tortilla_wrap, plain_flour, ground_almonds, baking_soda, baking_powder, salt, almond_milk,
                    caster_sugar, orange, vinegar, puff_pastry_sheet, apple_sauce, apple, maple_syrup, plant_based_milk,
                    ginger, tikka_curry_paste, light_brown_soft_sugar, cardamom_pods, brown_basmati_rice, raw_king_prawns,
                    double_cream, coriander, naan, chicken_thighs, lime, spring_onions, scotch_bonnet_chillies, thyme,
                    soy_sauce, vegetable_oil, allspice, white_basmati_rice, coconut_milk]
db.session.add_all(ingredients_list)


# Inserting values in IngredientRecipe table
# ingredients_in_recipe_ = IngredientRecipe(ingredient_recipe_measurement="", ingredient_id=, recipe_id=)

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
ingredients_in_recipe_31 = IngredientRecipe(ingredient_recipe_measurement="200g", ingredient_id=31, recipe_id=4)
ingredients_in_recipe_32 = IngredientRecipe(ingredient_recipe_measurement="50g", ingredient_id=32, recipe_id=4)
ingredients_in_recipe_33 = IngredientRecipe(ingredient_recipe_measurement="1 tsp", ingredient_id=33, recipe_id=4)
ingredients_in_recipe_34 = IngredientRecipe(ingredient_recipe_measurement="2 tsp", ingredient_id=34, recipe_id=4)
ingredients_in_recipe_35 = IngredientRecipe(ingredient_recipe_measurement="Pinch of", ingredient_id=35, recipe_id=4)
ingredients_in_recipe_36 = IngredientRecipe(ingredient_recipe_measurement="80ml", ingredient_id=26, recipe_id=4)
ingredients_in_recipe_37 = IngredientRecipe(ingredient_recipe_measurement="150ml", ingredient_id=36, recipe_id=4)
ingredients_in_recipe_38 = IngredientRecipe(ingredient_recipe_measurement="175g", ingredient_id=37, recipe_id=4)
ingredients_in_recipe_39 = IngredientRecipe(ingredient_recipe_measurement="Juices from 2", ingredient_id=38, recipe_id=4)
ingredients_in_recipe_40 = IngredientRecipe(ingredient_recipe_measurement="Zest from an", ingredient_id=38, recipe_id=4)
ingredients_in_recipe_41 = IngredientRecipe(ingredient_recipe_measurement="1 tbsp", ingredient_id=39, recipe_id=4)
ingredients_in_recipe_42 = IngredientRecipe(ingredient_recipe_measurement="1", ingredient_id=40, recipe_id=5)
ingredients_in_recipe_43 = IngredientRecipe(ingredient_recipe_measurement="1/4 cup", ingredient_id=41, recipe_id=5)
ingredients_in_recipe_44 = IngredientRecipe(ingredient_recipe_measurement="2", ingredient_id=42, recipe_id=5)
ingredients_in_recipe_45 = IngredientRecipe(ingredient_recipe_measurement="3 tbsp", ingredient_id=43, recipe_id=5)
ingredients_in_recipe_46 = IngredientRecipe(ingredient_recipe_measurement="3 tbsp", ingredient_id=44, recipe_id=5)
ingredients_in_recipe_47 = IngredientRecipe(ingredient_recipe_measurement="1", ingredient_id=1, recipe_id=6)
ingredients_in_recipe_48 = IngredientRecipe(ingredient_recipe_measurement="thumb-sized piece, peeled and grated", ingredient_id=45, recipe_id=6)
ingredients_in_recipe_49 = IngredientRecipe(ingredient_recipe_measurement="2 large", ingredient_id=3, recipe_id=6)
ingredients_in_recipe_50 = IngredientRecipe(ingredient_recipe_measurement="1 tbsp", ingredient_id=26, recipe_id=6)
ingredients_in_recipe_51 = IngredientRecipe(ingredient_recipe_measurement="2-3 tbsp", ingredient_id=46, recipe_id=6)
ingredients_in_recipe_52 = IngredientRecipe(ingredient_recipe_measurement="400g can", ingredient_id=10, recipe_id=6)
ingredients_in_recipe_53 = IngredientRecipe(ingredient_recipe_measurement="2 tbsp", ingredient_id=14, recipe_id=6)
ingredients_in_recipe_54 = IngredientRecipe(ingredient_recipe_measurement="1/2 tbsp", ingredient_id=47, recipe_id=6)
ingredients_in_recipe_55 = IngredientRecipe(ingredient_recipe_measurement="3, bashed", ingredient_id=48, recipe_id=6)
ingredients_in_recipe_56 = IngredientRecipe(ingredient_recipe_measurement="200g", ingredient_id=49, recipe_id=6)
ingredients_in_recipe_57 = IngredientRecipe(ingredient_recipe_measurement="3 tbsp", ingredient_id=32, recipe_id=6)
ingredients_in_recipe_58 = IngredientRecipe(ingredient_recipe_measurement="300g", ingredient_id=50, recipe_id=6)
ingredients_in_recipe_59 = IngredientRecipe(ingredient_recipe_measurement="1 tbsp", ingredient_id=51, recipe_id=6)
ingredients_in_recipe_60 = IngredientRecipe(ingredient_recipe_measurement="½ bunch, roughly chopped", ingredient_id=52, recipe_id=6)
ingredients_in_recipe_61 = IngredientRecipe(ingredient_recipe_measurement="Warmed, to serve (optional)", ingredient_id=53, recipe_id=6)
ingredients_in_recipe_62 = IngredientRecipe(ingredient_recipe_measurement="12", ingredient_id=54, recipe_id=7)
ingredients_in_recipe_63 = IngredientRecipe(ingredient_recipe_measurement="1", ingredient_id=55, recipe_id=7)
ingredients_in_recipe_64 = IngredientRecipe(ingredient_recipe_measurement="1 big bunch", ingredient_id=56, recipe_id=7)
ingredients_in_recipe_65 = IngredientRecipe(ingredient_recipe_measurement="Thumb sized piece", ingredient_id=45, recipe_id=7)
ingredients_in_recipe_66 = IngredientRecipe(ingredient_recipe_measurement="3", ingredient_id=3, recipe_id=7)
ingredients_in_recipe_67 = IngredientRecipe(ingredient_recipe_measurement="0.5", ingredient_id=1, recipe_id=7)
ingredients_in_recipe_68 = IngredientRecipe(ingredient_recipe_measurement="3", ingredient_id=57, recipe_id=7)
ingredients_in_recipe_69 = IngredientRecipe(ingredient_recipe_measurement="0.5 dried bunch", ingredient_id=58, recipe_id=7)
ingredients_in_recipe_70 = IngredientRecipe(ingredient_recipe_measurement="1", ingredient_id=55, recipe_id=7)
ingredients_in_recipe_71 = IngredientRecipe(ingredient_recipe_measurement="2 tbsp", ingredient_id=59, recipe_id=7)
ingredients_in_recipe_72 = IngredientRecipe(ingredient_recipe_measurement="2 tbsp", ingredient_id=60, recipe_id=7)
ingredients_in_recipe_73 = IngredientRecipe(ingredient_recipe_measurement="3 tbsp", ingredient_id=47, recipe_id=7)
ingredients_in_recipe_74 = IngredientRecipe(ingredient_recipe_measurement="1 tbsp", ingredient_id=61, recipe_id=7)
ingredients_in_recipe_75 = IngredientRecipe(ingredient_recipe_measurement="200g", ingredient_id=62, recipe_id=7)
ingredients_in_recipe_76 = IngredientRecipe(ingredient_recipe_measurement="400g can", ingredient_id=63, recipe_id=7)
ingredients_in_recipe_77 = IngredientRecipe(ingredient_recipe_measurement="1 bunch", ingredient_id=56, recipe_id=7)
ingredients_in_recipe_78 = IngredientRecipe(ingredient_recipe_measurement="2 large sprigs", ingredient_id=58, recipe_id=7)
ingredients_in_recipe_79 = IngredientRecipe(ingredient_recipe_measurement="2 cloves", ingredient_id=3, recipe_id=7)
ingredients_in_recipe_80 = IngredientRecipe(ingredient_recipe_measurement="1sp ground", ingredient_id=61, recipe_id=7)
ingredients_in_recipe_81 = IngredientRecipe(ingredient_recipe_measurement="2 x 410g cans", ingredient_id=13, recipe_id=7)


ingredients_in_recipe_list = [ingredients_in_recipe_1, ingredients_in_recipe_2, ingredients_in_recipe_3,
                              ingredients_in_recipe_4, ingredients_in_recipe_5, ingredients_in_recipe_6,
                              ingredients_in_recipe_7, ingredients_in_recipe_8, ingredients_in_recipe_9,
                              ingredients_in_recipe_10, ingredients_in_recipe_11, ingredients_in_recipe_12,
                              ingredients_in_recipe_13, ingredients_in_recipe_14, ingredients_in_recipe_15,
                              ingredients_in_recipe_16, ingredients_in_recipe_17, ingredients_in_recipe_18,
                              ingredients_in_recipe_19, ingredients_in_recipe_20, ingredients_in_recipe_21,
                              ingredients_in_recipe_22, ingredients_in_recipe_23, ingredients_in_recipe_24,
                              ingredients_in_recipe_25, ingredients_in_recipe_26, ingredients_in_recipe_27,
                              ingredients_in_recipe_28, ingredients_in_recipe_29, ingredients_in_recipe_30,
                              ingredients_in_recipe_31, ingredients_in_recipe_32, ingredients_in_recipe_33,
                              ingredients_in_recipe_34, ingredients_in_recipe_35, ingredients_in_recipe_36,
                              ingredients_in_recipe_37, ingredients_in_recipe_38, ingredients_in_recipe_39,
                              ingredients_in_recipe_40, ingredients_in_recipe_41, ingredients_in_recipe_42,
                              ingredients_in_recipe_43, ingredients_in_recipe_44, ingredients_in_recipe_45,
                              ingredients_in_recipe_46, ingredients_in_recipe_47, ingredients_in_recipe_48,
                              ingredients_in_recipe_49, ingredients_in_recipe_50, ingredients_in_recipe_51,
                              ingredients_in_recipe_52, ingredients_in_recipe_53, ingredients_in_recipe_54,
                              ingredients_in_recipe_55, ingredients_in_recipe_56, ingredients_in_recipe_57,
                              ingredients_in_recipe_58, ingredients_in_recipe_59, ingredients_in_recipe_60,
                              ingredients_in_recipe_61, ingredients_in_recipe_62, ingredients_in_recipe_63,
                              ingredients_in_recipe_64,ingredients_in_recipe_65, ingredients_in_recipe_66,
                              ingredients_in_recipe_67, ingredients_in_recipe_68, ingredients_in_recipe_69,
                              ingredients_in_recipe_70, ingredients_in_recipe_71, ingredients_in_recipe_72,
                              ingredients_in_recipe_73, ingredients_in_recipe_74, ingredients_in_recipe_75,
                              ingredients_in_recipe_76, ingredients_in_recipe_77, ingredients_in_recipe_78,
                              ingredients_in_recipe_79, ingredients_in_recipe_80, ingredients_in_recipe_81]
db.session.add_all(ingredients_in_recipe_list)


# Inserting values into the User table
person1 = User(first_name='Jane', last_name='Smith', username='JSmith1977', email='jane1977@gmail.com', password='1234abcd')
person2 = User(first_name='Kanye', username='Westicles', email='kwest@gmail.com', password='abcd9876')
person3 = User(first_name='Mary', last_name='Berry', username='maryberry3', email='mberry@outlook.com', password='5678abcd')

db.session.add(person1)
db.session.add(person2)
db.session.add(person3)

# Inserting values into the Comment/Rating tables


comment1 = Comment(comment="I really like this recipe. Delicious!", user_id=1, recipe_id=1, time_created=datetime.now())
comment2 = Comment(comment="I didn't enjoy this recipe. Won't be making it again.", user_id=1, recipe_id=2, time_created=datetime.now())
comment3 = Comment(comment="I enjoy this recipe. Won't be making it again.", user_id=1, recipe_id=3, time_created=datetime.now())
comment4 = Comment(comment="I could've come up with a much better recipe than this to be honest. Glad I used up the red pepper I had in the fridge though. X", user_id=3, recipe_id=1, time_created=datetime.now())
comment5 = Comment(comment="The most important thing is that a cake is moist. A delicious recipe.", user_id=3, recipe_id=4,time_created=datetime.now())

db.session.add(comment1)
db.session.add(comment2)
db.session.add(comment3)
db.session.add(comment4)

rating1 = Rating(rating=1, id=1, recipe_id=1)
rating2 = Rating(rating=1, id=2, recipe_id=2)
rating3 = Rating(rating=3, id=1, recipe_id=3)
rating4 = Rating(rating=4, id=1, recipe_id=4)
rating5 = Rating(rating=5, id=1, recipe_id=5)
rating6 = Rating(rating=4, id=3, recipe_id=4)

db.session.add(rating1)
db.session.add(rating2)
db.session.add(rating3)
db.session.add(rating4)
db.session.add(rating5)



# Inserting values into the Saved table

saved1 = SavedRecipe(user_id=1, recipe_id=1)
saved2 = SavedRecipe(user_id=1, recipe_id=5)

db.session.add(saved1)
db.session.add(saved2)

# Committing all the values into the database
db.session.commit()