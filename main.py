import webapp2
import jinja2
import os
import models
from models import Food_Meal

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

"""
def mealStringToUrl(meal_choice):
    imgUrl = ""
    jdata = ""
    if meal_choice == "burger":
        imgUrl = "http://img.thedailybeast.com/image/upload/v1493130772/galleries/2010/03/24/the-40-deadliest-fast-food-meals/fast-food---in-out-cheeseburger_bw2cot.jpg"
        ingredients = "bun","onion","patty","lettuce","tomato","cheese"
    elif meal_choice == "taco":
        imgUrl = "https://img1.cookinglight.timeinc.net/sites/default/files/styles/medium_2x/public/1519665233/slow-cooker-carnitas-tacos-ck-1804p38.jpg?itok=Kew1JNyq"
        ingredients = "tortilla","meat","salsa","onion","cilantro"
    elif meal_choice == "pasta":
        imgUrl = "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2015/9/15/1/FNK_Chicken-Fettucine-Alfredo_s4x3.jpg.rend.hgtvcom.826.620.suffix/1442375396342.jpeg"
        ingredients = "noodles","sauce","tomato","groundbeef"
    elif meal_choice == "sandwich":
        imgUrl = "https://indianakitchen.com/wp-content/uploads/2015/03/Ham-Sandwich.jpg"
        ingredients = "turkey","lettuce","tomato","mayo","bread"
    elif meal_choice == "salad":
        imgUrl = "https://www.tasteofhome.com/wp-content/uploads/2017/10/exps6498_MRR133247D07_30_5b_WEB-2.jpg"
        ingredients = "lettuce","spinach","tomato","croutons","ranch"
    elif meal_choice == "meatloaf":
        imgUrl = "https://images-gmi-pmc.edge-generalmills.com/3e0ded09-f8a2-45b6-aff7-e08ab138ed84.jpg"
        ingredients = "groundbeef","ketchup","onion","breadcrumbs"
    elif meal_choice == "enchiladas":
        imgUrl = "https://www.chilipeppermadness.com/wp-content/uploads/2019/02/Beef-Enchiladas-Recipe1.jpg"
        ingredients = "tortilla","groundbeef","cheese","redsauce"
    elif meal_choice == "stew":
        imgUrl = "https://www.simplyrecipes.com/wp-content/uploads/2015/03/irish-beef-stew-horiz-a2-1800.jpg"
        ingredients = "beef","potato","beefstock","carrot","peas"
    elif meal_choice == "pizza":
        imgUrl = "https://peopledotcom.files.wordpress.com/2019/02/gettyimages-938742222.jpg"
        ingredients = "dough","cheese","pepperoni","tomatosauce"
    elif meal_choice == "dumplings":
        imgUrl = "https://images-gmi-pmc.edge-generalmills.com/6059b986-4800-4508-8546-40cb56e3d815.jpg"
        ingredients = "flour","milk","butter","sugar","salt"
    elif meal_choice == "casserole":
        imgUrl = "https://images-gmi-pmc.edge-generalmills.com/fe6e9467-247e-4b3d-9694-973a818eeab1.jpg"
        jdata = "noodles","tomatosauce","cheese","breadcrumbs","groundbeef"
    elif meal_choice == "chile":
        imgUrl = "https://cdn-image.foodandwine.com/sites/default/files/styles/medium_2x/public/2012-r-xl-four-chile-chili.jpg?itok=_NWkr1bj"
        ingredients = "groundbeef","onion","greenpepper","tomatosauce","beans"
    elif meal_choice == "macNcheese":
        imgUrl = "https://www.tasteofhome.com/wp-content/uploads/2018/04/exps36313_TH1115229D39A.jpg"
        ingredients = "noodles","cheese","cheese","breadcrumbs","bacon"
    elif meal_choice == "hotdog":
        imgUrl = "https://a1.olivecache.net/assets/components/phpthumbof/cache/all_american_hot_dogs_small.bfce0e026efbc76dc3fab481a14cef02.jpg"
        ingredients = "sausage","cheese","bun","mustard","ketchup"
    else:
        imgUrl = ""
        ingredients = ""
    return imgUrl
"""
def ingredList(meal_choice):
    ingredients = ""
    if meal_choice == "burger":
        ingredients = "bun","onion","patty","lettuce","tomato","cheese"
    elif meal_choice == "taco":
        ingredients = "tortilla","meat","salsa","onion","cilantro"
    elif meal_choice == "pasta":
        ingredients = "noodles","sauce","tomato","groundbeef"
    elif meal_choice == "sandwich":
        ingredients = "turkey","lettuce","tomato","mayo","bread"
    elif meal_choice == "salad":
        ingredients = "lettuce","spinach","tomato","croutons","ranch"
    elif meal_choice == "meatloaf":
        ingredients = "groundbeef","ketchup","onion","breadcrumbs"
    elif meal_choice == "enchiladas":
        ingredients = "tortilla","groundbeef","cheese","redsauce"
    elif meal_choice == "stew":
        ingredients = "beef","potato","beefstock","carrot","peas"
    elif meal_choice == "pizza":
        ingredients = "dough","cheese","pepperoni","tomatosauce"
    elif meal_choice == "dumplings":
        ingredients = "flour","milk","butter","sugar","salt"
    elif meal_choice == "casserole":
        ingredients = "noodles","tomatosauce","cheese","breadcrumbs","groundbeef"
    elif meal_choice == "chile":
        ingredients = "groundbeef","onion","greenpepper","tomatosauce","beans"
    elif meal_choice == "macNcheese":
        ingredients = "noodles","cheese","cheese","breadcrumbs","bacon"
    elif meal_choice == "hotdog":
        ingredients = "sausage","cheese","bun","mustard","ketchup"
    else:
        ingredients = ""
    return ingredients



#MAIN PAGE WHERE USER IS FIRST AT

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(result_template.render())
#SECOND PAGE THAT THE USER WILL END UP AT
class ResultsPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(result_template.render())

    def post(self):
        mealChoiceFromForm = self.request.get("meal_choice")

    #    mealPictureFromFunction = mealStringToUrl(mealChoiceFromForm)
        mealIngredientsFromFunction = ingredList(mealChoiceFromForm)
        var_dict = {

            "meal_choice_dict_key": mealChoiceFromForm,
            #"meal_pic_dict_key": mealPictureFromFunction,
            "meal_ingredient_dict_key": mealIngredientsFromFunction
        }


        result_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(result_template.render(var_dict))

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/Results', ResultsPageHandler)

], debug=True)
