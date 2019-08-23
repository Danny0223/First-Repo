from google.appengine.ext import ndb

class Food_Meal(ndb.Model):
    name = ndb.StringProperty(required=True)
    ingredientList = ndb.StringProperty(required=True)

    # Burger = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="bun",
    #         ingred2="onion",
    #         ingred3="patty",
    #         ingred4="lettuce",
    #         ingred5="tomatoe",
    #         ingred6="cheese"
    #     ]
    # )
    #
    # Tacos = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="tortilla",
    #         ingred2="tortilla",
    #         ingred3="meat",
    #         ingred4="salsa",
    #         ingred5="onion",
    #         ingred6="cilantro"
    #     ]
    # )
    #
    # Pasta = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="Noodles",
    #         ingred2="S auce",
    #         ingred3="tomato",
    #         ingred4="groundbeef"
    #     ]
    # )
    #
    #  Sandwich = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="Turkey",
    #         ingred2="lettuce",
    #         ingred3="tomato",
    #         ingred4="bread",
    #         ingred5="Mayo"
    #     ]
    # )
    #
    #  Salad = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="lettuce",
    #         ingred2="spinach",
    #         ingred3="tomato",
    #         ingred4="croutons",
    #         ingred5="ranch",
    #     ]
    # )
    #
    #  meatloaf = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="groundbeef",
    #         ingred2="groundbeef",
    #         ingred3="ketcup",
    #         ingred4="onion",
    #         ingred5="breadcrumbs",
    #     ]
    # )
    #
    #  enchiladas = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="tortilla",
    #         ingred2="tortilla",
    #         ingred3="tortilla",
    #         ingred4="groundbeef",
    #         ingred5="cheese",
    #         ingred6="redsauce"
    #     ]
    # )
    #
    #  stew = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="beef",
    #         ingred2="potato",
    #         ingred3="beefstock",
    #         ingred4="carrot",
    #         ingred5="peas"
    #     ]
    # )
    #  pizza = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="dough",
    #         ingred2="cheese",
    #         ingred3="cheese",
    #         ingred4="pepperoni",
    #         ingred5="tomatosauce"
    #
    #     ]
    # )
    #
    #  dumplings = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="flour",
    #         ingred2="milk",
    #         ingred3="butter",
    #         ingred4="sugar",
    #         ingred5="salt"
    #     ]
    # )
    #
    #  casserole = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="noodles",
    #         ingred2="tomatosauce",
    #         ingred3="cheese",
    #         ingred4="breadcrumbs",
    #         ingred5="groundbeef",
    #         ]
    #     )
    #
    #  chili = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="groundbeef",
    #         ingred2="onion",
    #         ingred3="greenpepper",
    #         ingred4="tomatosauce",
    #         ingred5="beans"
    #
    #     ]
    # )
    #
    #  macNcheese = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="noodles",
    #         ingred2="cheese",
    #         ingred3="cheese",
    #         ingred4="breadcrumbs",
    #         ingred5="bacon"
    #
    #     ]
    # )
    #
    #  hotdog = Food_Meal(
    #     name = 'userMeal',
    #     ingredientList=[
    #         ingred1="sausage",
    #         ingred2="cheese",
    #         ingred3="bun",
    #         ingred4="mustard",
    #         ingred5="ketcup"
    #
    #     ]
    # )
