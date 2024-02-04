
import testing as t
from flask import Flask, render_template

app = Flask(__name__)
steps_list = t.getRecipe("chicken, sauce, beef, ostritch")
    # Assuming steps_list is defined somewhere in your code


@app.route('/')
def home():
    return render_template('testing.html', steps_list=steps_list)

if __name__ == '__main__':
    app.run(debug=True)
