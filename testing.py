import requests
import json


#link info
POSTS_API_URL = ""
main_url = "https://api.spoonacular.com/recipes/"
mode = "findByIngredients" 
API_key = "?apiKey=95613e06ce1c4cdf9e1044ba0bb8b510" 
arguments = "&ingredients="
argument_details = "" 
number_of_recipies = "&number=1"
#makes sure all elements in a string are formated into list seperated by commas

def format_list(items):
   ingredients =  [element.strip() for element in items.split(',')]
   return ingredients

#lists turns into a URL format

def format_List_of_ingredients(foods):
   result_string = ',+'.join(foods) 
   return result_string

#gets a list of 10 recipe names, 10 recipe IDs, and 10 recipe info dictionaries

def getRecipe_Info_FromIngredients(user_List_ingredients):
   recipes = []
   names = []
   ids = []
   num__missing_ingredients = []

   ingredients =  [element.strip() for element in user_List_ingredients.split(',')]
   argument_details =  format_List_of_ingredients(ingredients)
   POSTS_API_URL = main_url + mode + API_key + arguments + argument_details + number_of_recipies

   #request info based on URL, Convert to string

   Value_returned = requests.get(POSTS_API_URL)
   if Value_returned.status_code == 200:
      instructions = (Value_returned.text)
   else:
      print(f"Request failed with status code: {Value_returned.status_code}")

   #convert to Json dictionary and access recipe ID
   for dic in instructions:
      recipe_dict_list = json.loads(dic)
      Id = str(recipe_dict_list['id'])
      name = str(recipe_dict_list['title'])
      print(Id)
      print(name)
      recipes.append(dic)
      names.append(name)
      ids.append(Id)
   return names, ids, recipes

#gets a list recipe steps with a list of different recipe IDs

def getRecipe_steps(mul_id):
   recipes = []
   for Id in mul_id:
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
      recipes.append(steps_list)
   return recipes

#gather initial ingredients and format into url acceptable format

def getRecipe (input):
   ingredients =  [element.strip() for element in input.split(',')]
   argument_details =  format_List_of_ingredients(ingredients)
   POSTS_API_URL = main_url + mode + API_key + arguments + argument_details + number_of_recipies
   print(POSTS_API_URL)
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

class myClass:
   ingredients = []
   names = []
   ids = []
   recipes = []

   def __init__(self) -> None:
      temp_food = input("food in your pantry: ")
      self.foods = format_list(temp_food)
      self.names, self.ids, self.recipes = getRecipe_Info_FromIngredients(temp_food)
      list_of_recipe_instructions = getRecipe_steps(ids)
   def addfood(food_list):
      food = input("add food in your pantry: ")
      words = format_list(food)
      for word in words:
         if word not in foods:
            self.foods.append(word)


