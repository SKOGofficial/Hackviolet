import requests
import json

def ingredients_List(foods):
   result_string = ',+'.join(ingredients) 
   return result_string

#link info

POSTS_API_URL = ""
main_url = "https://api.spoonacular.com/recipes/"
mode = "findByIngredients" 
API_key = "?apiKey=95613e06ce1c4cdf9e1044ba0bb8b510" 
arguments = "&ingredients="
argument_details = "" 
number_of_recipies = "&number=1"

#gather initial ingredients and format into url acceptable format

response = input("What are the ingredients you have in your pantry make a list seperarated by commas ',' \n" )

ingredients =  [element.strip() for element in response.split(',')]
argument_details =  ingredients_List(ingredients)
POSTS_API_URL = main_url + mode + API_key + arguments + argument_details + number_of_recipies

#request info based on URL, Convert to string

Value_returned = requests.get(POSTS_API_URL)
if Value_returned.status_code == 200:
    instructions = (Value_returned.text)
else:
    print(f"Request failed with status code: {Value_returned.status_code}")

#convert to Json dictionary and access recipe ID

length =  len(instructions)
recipe_dict_list = json.loads(instructions[1:length -1])
Id = str(recipe_dict_list['id'])
print(Id)

#Request new information based on recipe ID, convert to JSON and print

POSTS_API_URL = main_url + Id + "/analyzedInstructions" + API_key
print(POSTS_API_URL)
returned = requests.get(POSTS_API_URL)
if returned.status_code == 200:
    instructions = (returned.text)
else:
    print(f"Request failed with status code: {returned.status_code}")

print(type(instructions))
length = len(instructions)
recipe = json.loads(instructions[1:length -1])
print(recipe)