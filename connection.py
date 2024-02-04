
import testing as t
from flask import Flask, render_template

app = Flask(__name__)
steps_list = t.getRecipe("lettuce, bread, chicken, bacon, olives")
    # Assuming steps_list is defined somewhere in your code


@app.route('/')
def home():
    return render_template('testing.html', steps_list=steps_list)

@app.route('/Home')
def home_page():
    return render_template('Home.html')

@app.route('/Inventory')
def inventory():
    return render_template('Inventory.html')

@app.route('/find_a_recipe')
def find_a_recipe():
    return render_template('find_a_recipe.html')

@app.route('/meals_ive_had')
def meals_ive_had():
    return render_template('meals_ive_had.html')


if __name__ == '__main__':
    app.run(debug=True)
