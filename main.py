from dinnerly import *
import json

d = Dinnerly()
info = d.get_account_information()
#past = d.get_past_recipes()
#current = d.get_recipes("current")

past_ids = []
past = d.get_recipes("past")

recipe_ids = []
print("=== PAST ===")
for i in past:
    for j in i["recipes"]:
        recipe_ids.append(j['id'])

print("== RECIPE ==")
past_recipes = []
for r in recipe_ids:
    recipe_info = {}
    recipe = d.get_recipe_information(r)
    #print("Meal Attributes for %s: " % recipe["name_with_subtitle"])
    recipe_info["name"] = recipe["name_with_subtitle"]
    meal_attributes = []
    for i in recipe["meal_attributes"]:
        #print(i)
        meal_attributes.append(i)
    recipe_info["attributes"] = meal_attributes
    #print("prep time")
    #print(recipe["preparation_time"])
    recipe_info["prep_time"] = recipe["preparation_time"]
    #print("ingredients")
    ingredients = []
    for i in recipe["ingredients"]:
        #print(i["name"])
        ingredients.append(i["name"])
    recipe_info["ingredients"] = ingredients
    past_recipes.append(recipe_info)

print(past_recipes)
f = open("dinnerly.txt", "a")
f.write(str(json.dumps(past_recipes)))
