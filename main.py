import webapp2
import jinja2
import os
import models
from models import Food_Meal

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def mealStringToUrl(meal_choice):
    imgUrl = ""
    if meal_choice == "burger":
        imgUrl = "http://img.thedailybeast.com/image/upload/v1493130772/galleries/2010/03/24/the-40-deadliest-fast-food-meals/fast-food---in-out-cheeseburger_bw2cot.jpg"
    elif meal_choice == "tacos":
        imgUrl = "https://img1.cookinglight.timeinc.net/sites/default/files/styles/medium_2x/public/1519665233/slow-cooker-carnitas-tacos-ck-1804p38.jpg?itok=Kew1JNyq"
    elif meal_choice == "pasta":
        imgUrl = "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2015/9/15/1/FNK_Chicken-Fettucine-Alfredo_s4x3.jpg.rend.hgtvcom.826.620.suffix/1442375396342.jpeg"
    elif meal_choice == "sandwich":
        imgUrl = "https://indianakitchen.com/wp-content/uploads/2015/03/Ham-Sandwich.jpg"
    elif meal_choice == "salad":
        imgUrl = "https://www.tasteofhome.com/wp-content/uploads/2017/10/exps6498_MRR133247D07_30_5b_WEB-2.jpg"
    elif meal_choice == "meatloaf":
        imgUrl = "https://images-gmi-pmc.edge-generalmills.com/3e0ded09-f8a2-45b6-aff7-e08ab138ed84.jpg"
    elif meal_choice == "enchiladas":
        imgUrl = "https://www.chilipeppermadness.com/wp-content/uploads/2019/02/Beef-Enchiladas-Recipe1.jpg"
    elif meal_choice == "stew":
        imgUrl = "https://www.simplyrecipes.com/wp-content/uploads/2015/03/irish-beef-stew-horiz-a2-1800.jpg"
    elif meal_choice == "pizza":
        imgUrl = "https://peopledotcom.files.wordpress.com/2019/02/gettyimages-938742222.jpg"
    elif meal_choice == "dumplings":
        imgUrl = "https://images-gmi-pmc.edge-generalmills.com/6059b986-4800-4508-8546-40cb56e3d815.jpg"
    elif meal_choice == "casserole":
        imgUrl = "https://images-gmi-pmc.edge-generalmills.com/fe6e9467-247e-4b3d-9694-973a818eeab1.jpg"
    elif meal_choice == "chile":
        imgUrl = "https://cdn-image.foodandwine.com/sites/default/files/styles/medium_2x/public/2012-r-xl-four-chile-chili.jpg?itok=_NWkr1bj"
    elif meal_choice == "macNcheese":
        imgUrl = "https://www.tasteofhome.com/wp-content/uploads/2018/04/exps36313_TH1115229D39A.jpg"
    elif meal_choice == "hotdog":
        imgUrl = "https://a1.olivecache.net/assets/components/phpthumbof/cache/all_american_hot_dogs_small.bfce0e026efbc76dc3fab481a14cef02.jpg"
    else:
        imgUrl = ""
    return imgUrl

def mealCalories(meal_choice):
    calories = ""
    if meal_choice == "burger":
        calories = "596"
    elif meal_choice == "tacos":
        calories = "492"
    elif meal_choice == "pasta":
        calories = "587"
    elif meal_choice == "sandwich":
        calories = "203"
    elif meal_choice == "salad":
        calories = "183"
    elif meal_choice == "meatloaf":
        calories = "809"
    elif meal_choice == "enchiladas":
        calories = "857"
    elif meal_choice == "stew":
        calories = "448"
    elif meal_choice == "pizza":
        calories = "222"
    elif meal_choice == "dumplings":
        calories = "333"
    elif meal_choice == "casserole":
        calories = "444"
    elif meal_choice == "chile":
        calories = "555"
    elif meal_choice == "macNcheese":
        calories = "666"
    elif meal_choice == "hotdog":
        calories = "777"
    else:
        calories = ""
    return calories

def mealIngred(meal_choice):
    ingred = ""
    if meal_choice == "burger":
        ingred = "<h1>bun:133<br>onion:32<br>groundbeef:336<br>lettuce:10<br>tomato:22<br>cheese:63</h1>"
    elif meal_choice == "tacos":
        ingred = "<h1>tortilla:112<br>groundbeef:336<br>salse:10<br>onion:32<br>cilantro:22</h1>"
    elif meal_choice == "pasta":
        ingred = "<h1>noodles:200<br>tomatosauce:29<br>tomato:22<br>groundbeef:336</h1>"
    elif meal_choice == "sandwich":
        ingred = "<h1>turnkey:45<br>lettuce:10<br>tamato:22<br>bread:69<br>mayo:57</h1>"
    elif meal_choice == "salad":
        ingred = "<h1>lettuce:75<br>spinach:7<br>choppoedtamto:10<br>croutons:31<br>ranch:60</h1>"
    elif meal_choice == "meatloaf":
        ingred = "<h1>groundbeef:336<br>groundbeef:336<br>ketcup:15<br>ketchup:15<br>onion:32<br>breadcrumbs:107</h1>"
    elif meal_choice == "enchiladas":
        ingred = "<h1>tortilla:112<br>tortilla:112<br>tortilla:112<br>groundbeef:336<br>cheese:120<br>redsauce:65</h1>"
    elif meal_choice == "stew":
        ingred = "<h1>beef:256<br>potatoe:67<br>beefstock:31<br>carrot:27<br>peas:67</h1>"
    elif meal_choice == "pizza":
        ingred = "<h1>dough:160<br>cheese:340<br>pepperoni:200<br>tomatosauce:29</h1>"
    elif meal_choice == "dumplings":
        ingred = "<h1>flour:104<br>milk:149<br>butter:150<br>sugar:17</h1>"
    elif meal_choice == "casserole":
        ingred = "<h1>noodles:209<br>tomatosauce:29<br>mozzarella:348<br>breadcrumbs:107<br>groundbeef:336</h1>"
    elif meal_choice == "chili":
        ingred = "<h1>groundbeef:336<br>onion:32<br>greenpepper:38<br>tomatosauce:29<br>beans:112</h1>"
    elif meal_choice == "macNcheese":
        ingred = "<h1>noodles:209<br>mozzarella:348<br>breadcrumbs:107<br>bacon:43</h1>"
    elif meal_choice == "hotdog":
        ingred = "<h1>sausage:209<br>cheese:63<br>sausageBun:144<br>mustard<br>mustard=8<br>ketchup:16</h1>"
    else:
        ingred = ""
    return ingred


#MAIN PAGE WHERE USER IS FIRST AT

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(result_template.render())
#SECOND PAGE THAT THE USER WILL END UP AT
"""
class BurgerHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/burger.html')
        self.response.write(result_template.render())
"""



class ResultsPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(result_template.render())

    def post(self):
        mealChoiceFromForm = self.request.get("meal_choice")

        mealPictureFromFunction = mealStringToUrl(mealChoiceFromForm)

        mealCaloriesFromFunction = mealCalories(mealChoiceFromForm)

        mealIngredFromFunction = mealIngred(mealChoiceFromForm)

        var_dict = {
            "meal_choice_dict_key": mealChoiceFromForm,
            "meal_pic_dict_key":mealPictureFromFunction,
            "meal_calories_dict_key": mealCaloriesFromFunction
        }

        result_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(result_template.render(var_dict))
        self.response.write(mealIngredFromFunction)

"""
class BlogHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/new_post.html')
        self.response.write(result_template.render())
"""
"""
        meal1.put()
"""

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/Results', ResultsPageHandler),
    #('/burgers',BurgerHandler),
    #('/tacos',TacosHandler),
    #('/pasta',PastaHandler),
    #('/sandwich',SandwichHandler),
    #('/salad',SaladHandler),
    #('/meatloaf',MeatloafHandler),
    #('/enchiladas',EnchiladasHandler),
    #('/stew',StewHandler),
    #('/pizza',PizzaHandler),
    #('/dumplings',DumplingsHandler),
    #('/casserole',CasseroleHandler),
    #('/chile',ChileHandler),
    #('/macncheese',MacNCheeseHandler),
    #('/hotdogs',HotDogHandler),
    #('/view_all_meals',ViewHandler)
    #('/Results', ResultsPageHandler)


], debug=True)
