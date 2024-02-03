import requests

def ingredients_List(foods):
   result_string = ',+'.join(ingredients) 
   return result_string

# POSTS_API_URL = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=95613e06ce1c4cdf9e1044ba0bb8b510&ingredients=apples,+flour,+sugar&number=2"
# main_url = "https://api.spoonacular.com/recipes/"
# mode = "findByIngredients" #different modes available, make method for this
# API_key = "?apiKey=95613e06ce1c4cdf9e1044ba0bb8b510" #for convinience make an insert API Key method for later
# arguments = "&ingredients="
# argument_details = "apples,+flour,+sugar" #a little bit more complicated because arguments depends on the mode, Save for later
# number_of_recipies = "&number="
# number = "1"

# response = input("What are the ingredients you have in your pantry\nmake a list seperarated by commas ',' \n" )
# ingredients =  [element.strip() for element in response.split(',')]

     
# argument_details =  ingredients_List(ingredients)
# POSTS_API_URL = main_url + mode + API_key + arguments + argument_details + number_of_recipies + number
# response = requests.get(POSTS_API_URL)
# if response.status_code == 200:
#     print(response.text)
# else:
#     print(f"Request failed with status code: {response.status_code}")
import json

json_string = '[{"id":638604,"title":"Chilled Swiss Oatmeal","image":"https://spoonacular.com/recipeImages/638604-312x231.jpg","imageType":"jpg","usedIngredientCount":2,"missedIngredientCount":5,"missedIngredients":[{"id":8121,"amount":0.5,"unit":"cup","unitLong":"cups","unitShort":"cup","aisle":"Cereal","name":"old-fashioned oatmeal","original":"1/2 cup old-fashioned oatmeal (may use steel cut but not the instant kind)","originalName":"old-fashioned oatmeal (may use steel cut but not the instant kind)","meta":["instant","(may use steel cut but not the kind)"],"image":"https://spoonacular.com/cdn/ingredients_100x100/rolled-oats.jpg"},{"id":1001119,"amount":6.0,"unit":"oz","unitLong":"ounces","unitShort":"oz","aisle":"Milk, Eggs, Other Dairy","name":"vanilla yogurt","original":"6 oz low-fat vanilla yogurt (if using plain yogurt, add honey for sweetness)","originalName":"low-fat vanilla yogurt (if using plain yogurt, add honey for sweetness)","meta":["plain","low-fat","for sweetness","(if using yogurt, add honey )"],"extendedName":"low fat plain vanilla yogurt","image":"https://spoonacular.com/cdn/ingredients_100x100/vanilla-yogurt.png"},{"id":1077,"amount":0.33333334,"unit":"cup","unitLong":"cups","unitShort":"cup","aisle":"Milk, Eggs, Other Dairy","name":"milk","original":"1/3 cup milk","originalName":"milk","meta":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/milk.png"},{"id":9078,"amount":2.0,"unit":"tablespoon","unitLong":"tablespoons","unitShort":"Tbsp","aisle":"Produce","name":"cranberry","original":"2-3 tablespoon dried cranberry or raisins","originalName":"dried cranberry or raisins","meta":["dried"],"extendedName":"dried cranberry","image":"https://spoonacular.com/cdn/ingredients_100x100/cranberries.jpg"},{"id":12155,"amount":1.0,"unit":"tablespoon","unitLong":"tablespoon","unitShort":"Tbsp","aisle":"Baking","name":"walnuts","original":"1 tablespoon walnuts","originalName":"walnuts","meta":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/walnuts.jpg"}],"usedIngredients":[{"id":9003,"amount":1.0,"unit":"small","unitLong":"small","unitShort":"small","aisle":"Produce","name":"apple","original":"1 small apple, chopped","originalName":"apple, chopped","meta":["chopped"],"image":"https://spoonacular.com/cdn/ingredients_100x100/apple.jpg"},{"id":9040,"amount":1.0,"unit":"small","unitLong":"small","unitShort":"small","aisle":"Produce","name":"banana","original":"1 small banana, chopped","originalName":"banana, chopped","meta":["chopped"],"image":"https://spoonacular.com/cdn/ingredients_100x100/bananas.jpg"}],"unusedIngredients":[{"id":9200,"amount":1.0,"unit":"serving","unitLong":"serving","unitShort":"serving","aisle":"Produce","name":"orange","original":"orange","originalName":"orange","meta":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/orange.png"}],"likes":7}]'

# Convert JSON string to a Python dictionary
recipe_dict_list = json.loads(json_string)

print(recipe_dict_list['title'])

# Print the resulting dictionary
print(recipe_dict_list)
