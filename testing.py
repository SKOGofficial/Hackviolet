import requests
import json

def ingredients_List(foods):
   result_string = ',+'.join(foods) 
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

def getRecipe (input):
   ingredients =  [element.strip() for element in input.split(',')]
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
   name = str(recipe_dict_list['title'])

   print(Id)
   print(name)
   #Request new information based on recipe ID, convert to JSON and print

   POSTS_API_URL = main_url + Id + "/analyzedInstructions" + API_key
   print(POSTS_API_URL)
   returned = requests.get(POSTS_API_URL)
   if returned.status_code == 200:
      instructions = (returned.text)
   else:
      print(f"Request failed with status code: {returned.status_code}")

   length = len(instructions)
   recipe = json.loads(instructions[1:length -1])

   steps_list = []

   for steps in recipe['steps']:
      instruction = steps['step']
      steps_list.append(instruction)
   return steps_list

