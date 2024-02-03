print("heee")
print("Sean")
print("Soham, testing")
print("testing for Kim!!!")

print("Sean Testing again hehehehehe")

print("testing for lakshitha !!!!!!!!! :) :) :0 school account :(")
import requests

POSTS_API_URL = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=95613e06ce1c4cdf9e1044ba0bb8b510&ingredients=apples,+flour,+sugar&number=2"

response = requests.get(POSTS_API_URL)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Request failed with status code: {response.status_code}")
