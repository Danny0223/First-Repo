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
    elif meal_choice == "taco":
        imgUrl = "https://media1.tenor.com/images/cfeb7a77e287d674d56d4706dcaeab1c/tenor.gif?itemid=5446149"
    elif meal_choice == "pasta":
        imgUrl = "https://66.media.tumblr.com/c6547a1ce571b9432cfba47b5fac538f/tumblr_pn06z5RAz51wt43j1_540.jpg"
    else:
        imgUrl = ""
    return imgUrl

#MAIN PAGE WHERE USER IS FIRST AT

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(result_template.render())
#SECOND PAGE THAT THE USER WILL END UP AT
class BurgerHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/burger.html')
        self.response.write(result_template.render())




class ResultsPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(result_template.render())

<<<<<<< HEAD
    def post(self):
        mealChoiceFromForm = self.request.get("meal_choice")

        mealPictureFromFunction = mealStringToUrl(mealChoiceFromForm)





        var_dict = {
            "meal_choice_dict_key": mealChoiceFromForm,
            "meal_pic_dict_key":mealPictureFromFunction
        }

        result_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(result_template.render(var_dict))

"""
class BlogHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/new_post.html')
        self.response.write(result_template.render())
"""
=======
>>>>>>> 224fcbe88fb0a230e8a30479669e027dd4c932ed

#DISPLAY TOOL
class ViewHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/view_all_meals.html')
        self.response.write(result_template.render())
"""
        meal1= Food_Meal(name = Choose_Your_Meal)
        meal1.put()
"""

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
<<<<<<< HEAD
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
    ('/view_all_meals',ViewHandler),
=======
    ('/Results', ResultsPageHandler)
>>>>>>> 224fcbe88fb0a230e8a30479669e027dd4c932ed

], debug=True)
