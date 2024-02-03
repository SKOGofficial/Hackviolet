import requests
import json

def ingredients_List(foods):
   result_string = ',+'.join(ingredients) 
   return result_string

POSTS_API_URL = ""
main_url = "https://api.spoonacular.com/recipes/"
mode = "findByIngredients" #different modes available, make method for this
API_key = "?apiKey=95613e06ce1c4cdf9e1044ba0bb8b510" #for convinience make an insert API Key method for later
arguments = "&ingredients="
argument_details = "" #a little bit more complicated because arguments depends on the mode, Save for later
number_of_recipies = "&number=1"

response = input("What are the ingredients you have in your pantry\nmake a list seperarated by commas ',' \n" )

#going from response to getting values
#getting recipe ID and missing ingredients, extra ingredients and the rest of the matrerials 
ingredients =  [element.strip() for element in response.split(',')]
argument_details =  ingredients_List(ingredients)
POSTS_API_URL = main_url + mode + API_key + arguments + argument_details + number_of_recipies

Value_returned = requests.get(POSTS_API_URL)
if Value_returned.status_code == 200:
    instructions = (Value_returned.text)
else:
    print(f"Request failed with status code: {Value_returned.status_code}")


print(type(instructions))

#using the ID to find the recipe instrictions 
# Convert JSON string to a Python list of dictionaries
length =  len(instructions)
recipe_dict_list = json.loads(instructions[1:length -1])
Id = str(recipe_dict_list['id'])

POSTS_API_URL = main_url + Id + "/analyzedInstructions"

returned = requests.get(POSTS_API_URL)
if returned.status_code == 200:
    instructions = (returned.text)
else:
    print(f"Request failed with status code: {returned.status_code}")

print(type(instructions))
length = len(instructions)
recipe = json.loads(instructions[1:length -1])
print(recipe)