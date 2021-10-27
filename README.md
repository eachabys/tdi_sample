# The dataset
The dataset can be found https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions?select=RAW_recipes.csv
It was part of the food.com interactions and contain more than 700 recipes which will be used for this project.

# The Goal
The goal is to analyze the product and help the users to pick the most suitable recipe according to their needs, including the names of the ingredients, their maximum number, maximum cooking time, and special tags, such as dietary, gluten-free,and so on. A possible solution may be presented using the above mentioned 4 parameters: https://eachabys.wixsite.com/kert 

# The Analysis
These two graphs represent preliminry analysis of the data.
The first notebook time_quantity.ipynb includes an analysis of how much time it takes to cook any recipe. The graph shows how many meal recipes which can be cooked in 5, 10, 15, ... minutes. For ease, only the recipes f the meals which can be cooked in 2h or 120 minutes are considered. The cooking time is rounded to the nearest 5 minutes.
The other notebook ingredients_quantity.ipynb includes an analysis of how many ingredients are used in a recipe. The resulting graph shows how many meal recipes  which contain only 2,3,4,... ingredients to cook a meal. Here, it seems that the most meals can be cooked with 10 variable ingredients. The data shows that the majority of recipes can be cooked with less than 20 ingredients.
