<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Hokie Feast</title>
   <style>
       body {
           font-family: Arial, sans-serif;
           margin: 0;
           padding: 0;
           background-color: #f0f0f0;
           overflow-y: scroll; /* Add overflow-y property to enable vertical scroll */
       }
       header {
           background-color: #630031;
           color: #fff;
           padding: 10px;
           text-align: center;
           position: relative; /* Add position relative to header */
       }
       .login-button {
           position: absolute;
           top: 10px;
           right: 10px;
           color: #fff;
           text-decoration: none;
           padding: 15px 20px;
           background-color: #CF4420;
           border-radius: 5px;
       }
       nav {
           background-color: #CF4420;
           padding: 10px;
           text-align: center;
           list-style-type: none;
       }
       nav a {
           color: #fff;
           text-decoration: none;
           padding: 5px 10px;
           margin: 0 5px;
       }
       nav a:hover {
           background-color: #666;
       }
       #menu-meals{
           display:inline-block;
           list-style-type: none;
           padding:5px;
       }
       
       section {
           padding: 20px;
       }
       footer {
           background-color: #630031;
           color: #fff;
           padding: 10px;
           text-align: center;
           position: fixed;
           bottom: 0;
           width: 100%;
       }
       a {
        color:#CF4420;
       }
   </style>
</head>
<body>
   <header>
       <h1>Welcome to Hokie Feast</h1>
       <a href="login.html" class="login-button">Login</a> <!-- Login button -->
   </header>
   <nav>

       <a href="Home.html">Home</a>
       <a href="Inventory.html">Inventory</a>
       <a href="find_a_recipe.html">Find a Recipe</a>
       <a href="meals_ive_had.html">Meals I've Had</a>
       
   </nav>
   <section>
       <h2>About Us</h2>
       <p>
            Hokie Feast is a student-made student made website to help people 
            find recipes for ingredients they already have. Now, when you're
            at home and unsure of what to cook, we can give you some ideas!
        </p>
        <h2>How to Use Our Website</h2>
        <p>
            First, go to the inventory page and select all the items you have 
            in your fridge and pantry. Then, go to the <a href="find_a_recipe.html">"Find a Recipe"</a> page
            and find a reccipe that you can start preparing with the tools
            you already have.
        </p>
   </section>
   <footer>
       <p>&copy; 2024 Hokie Feast. All rights reserved.</p>
   </footer>
</body>
</html>