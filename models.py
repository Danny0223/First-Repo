from google.appengine.ext import ndb

class Food_Meal(ndb.Model):
    name = ndb.StringProperty(required=True)
    ingredientList = ndb.StringProperty(required=True)
"""
    Burger = Food_Meal(
        name = 'userMeal',
        ingredientList=[

        ]
    )
"""
