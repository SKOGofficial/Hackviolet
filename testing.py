
import requests

POSTS_API_URL = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=95613e06ce1c4cdf9e1044ba0bb8b510&ingredients=apples,+flour,+sugar&number=2"
main_url = "https://api.spoonacular.com/recipes/"
mode = "findByIngredients" #different modes available, make method for this
API_key = "?apiKey=95613e06ce1c4cdf9e1044ba0bb8b510" #for convinience make an insert API Key method for later
arguments = "&ingredients=apples,+flour,+sugar&number=2" #a little bit more complicated because arguments depends on the mode, Save for later
# response = requests.get(POSTS_API_URL)
# if response.status_code == 200:
#     print(response.text)
# else:
#     print(f"Request failed with status code: {response.status_code}")
response = input("What are the ingredients you have in your pantry\nmake a list seperarated by commas ',' \n" )
ingredients =  [element.strip() for element in response.split(',')]
print(ingredients)
