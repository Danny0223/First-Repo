
ssssssssssssssssssssssssssssssssssimport webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class Meal(object):
    def __init__(self, _name, _ingredientList):
        self.name = _name
        self.ingredientList = _ingredientList
        var_dict=
            [
                {
                    name:"Burger"
                        [
                            ingred1:"bun"
                            ingred2:"onion"
                            ingred3:"patty"
                            ingred4:"lettuce"
                            ingred5:"tomatoe"
                        ],
                    name:"Taco"
                        [
                            ingred1:"tortilla"
                            ingred2:"meat"
                        ],
                    name:"Burrito"
                        [
                            ingred1:"tortilla"
                            ingred2:"beans"
                            ingred3:"meat"
                            ingred4:"rice"
                            ingred5:"cheese"
                            ingred6:"lettuce"
                            ingred7:"sourCream"
                        ],
                    name:"Chicken Alfredo"
                        [
                            ingred1:"boneless chicken"
                            ingred2:"fettucine"
                            ingred3:"garlic"
                            ingred4:"sauce"
                        ],
                    name:"Sandwich"
                        [
                            ingred1:"bread"
                            ingred2:"turkey"
                            ingred3:"cheese"
                            ingred4:"tomatoe"
                            ingred5:"mayo"
                            ingred6:"lettuce"
                        ],
                    name:"Salad"
                        [
                            ingred1:"lettuce"
                            ingred2:"spinage"
                            ingred3:"tomatoe"
                            ingred4:"cruton"
                            ingred5:"carrot"
                        ],
                    name:"Meatloaf"
                        [
                            ingred1:"groundbeef"
                            ingred2:"bread crumbs"
                            ingred3:"onion"
                            ingred4:"milk"
                            ingred5:"egg"
                            ingred6:"ketchup"
                            ingred7:"sauce"
                            ingred8:"parsley"
                            ingred9:"garlic powder"
                            ingred10:"salt"
                            ingred11:"pepper"
                        ]
                }




            ]
m1 = Meal("Burger",)
"""
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        welcome_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(welcome_template.render())

class FoodInfoHandler(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('templates/Burgers.html')
        self.response.write(results_template.render())

"""


app = webapp2.WSGIApplication([
    ('/',EnterInfoHandler ),
    ('/danny',FoodInfoHandler)
], debug=True)
