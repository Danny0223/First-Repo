from google.appengine.ext import ndb

class Food_Meal(ndb.Model):
    name = ndb.StringProperty(required=True)
    ingredientList = ndb.StringProperty(required=True)

    Burger = Food_Meal(
        name = 'userMeal',
        ingredientList=[
            ingred1="bun"
            ingred2="onion"
            ingred3="patty"
            ingred4="lettuce"
            ingred5="tomatoe"
        ]
    )

    Tacos = Food_Meal(
        name = 'userMeal',
        ingredientList=[
            ingred1="tortilla"
            ingred2="meat"
        ]
    )

    Pasta = Food_Meal(
        name = 'userMeal',
        ingredientList=[
            ingred1=""
            ingred2=""

        ]
    )

     = Food_Meal(
        name = 'userMeal',
        ingredientList=[
            ingred1=""
            ingredd2=""

        ]
    )

     = Food_Meal(
        name = 'userMeal',
        ingredientList=[
            ingred1=""
            ingredd2=""

        ]
    )

     = Food_Meal(
        name = 'userMeal',
        ingredientList=[
            ingred1=""
            ingredd2=""

        ]
    )

     = Food_Meal(
        name = 'userMeal',
        ingredientList=[
            ingred1=""
            ingredd2=""

        ]
    )

     = Food_Meal(
        name = 'userMeal',
        ingredientList=[
            ingred1=""
            ingredd2=""

        ]
    )
