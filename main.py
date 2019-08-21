
import webapp2
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
                            ingred1:"bun",
                            ingred2:"onion",
                            ingred3:"patty",
                            ingred4:"lettuce",
                            ingred5:"tomatoe"
                        ],
                    name:"Taco"
                        [
                            ingred1:"tortilla",
                            ingred2:"meat"
                        ],
                    name:"Burrito"
                        [
                            ingred1:"tortilla",
                            ingred2:"beans",
                            ingred3:"meat",
                            ingred4:"rice",
                            ingred5:"cheese",
                            ingred6:"lettuce",
                            ingred7:"sourCream"
                        ],
                    name:"Chicken Alfredo"
                        [
                            ingred1:"boneless chicken",
                            ingred2:"fettucine",
                            ingred3:"garlic",
                            ingred4:"sauce"
                        ],
                    name:"Sandwich"
                        [
                            ingred1:"bread",
                            ingred2:"turkey",
                            ingred3:"cheese",
                            ingred4:"tomatoe",
                            ingred5:"mayo",
                            ingred6:"lettuce"
                        ],
                    name:"Salad"
                        [
                            ingred1:"lettuce",
                            ingred2:"spinage",
                            ingred3:"tomatoe",
                            ingred4:"cruton",
                            ingred5:"carrot"
                        ],
                    name:"Meatloaf"
                        [
                            ingred1:"groundbeef",
                            ingred2:"bread crumbs",
                            ingred3:"onion",
                            ingred4:"milk",
                            ingred5:"egg",
                            ingred6:"ketchup",
                            ingred7:"sauce",
                            ingred8:"parsley",
                            ingred9:"garlic powder",
                            ingred10:"salt",
                            ingred11:"pepper"
                        ],
                    name:"Enchiladas"
                        [
                            ingred1:"groundbeef",
                            ingred2:"tortilla",
                            ingred3:"onion",
                            ingred4:"sauce",
                            ingred5:"cheese",
                            ingred6:"green chiles"
                        ],
                    name:"Stew"
                        [
                            ingred1:"beef",
                            ingred2:"onion",
                            ingred3:"carrot",
                            ingred4:"garlic",
                            ingred5:"tamato",
                            ingred6:"peas",
                            ingred7:"sauce",
                            ingred8:"potatoes",
                            ingred9:"veggie broth",
                            ingred10:"salt",
                            ingred11:"pepper"
                        ],
                    name:"Pizza"
                        [
                            ingred1:"dough",
                            ingred2:"tomato sauce",
                            ingred3:"cheese",
                            ingred4:"pepperoine",
                        ],
                    name:"Dumplings"
                        [
                            ingred1:"flour",
                            ingred2:"baking powder",
                            ingred3:"salt",
                            ingred4:"milk",
                            ingred5:"butter"
                        ],
                    name:"Casserole"
                        [
                            ingred1:"red peppers"
                            ingred2:"tomato sauce"
                            ingred3:"zucchini"
                            ingred4:"squash"
                            ingred5:"mushrooms"
                            ingred6:"pasta"
                        ],
                    name:"Chile"
                        [
                            ingred1:"groundbeef"
                            ingred2:"tomato sauce"
                            ingred3:"cheese"
                            ingred4:"green pepper"
                            ingred5:"beans"
                            ingred6:"garlic"
                        ],
                    name:"MacNCheese"
                        [
                            ingred1:"Pasta"
                            ingred2:"breed crumbs"
                            ingred3:"cheese"
                            ingred4:"cheese"
                            ingred4:"milk"
                        ],
                    name:"Hot dog"
                        [
                            ingred1:"bread"
                            ingred2:"sausage"
                            ingred3:"cheese"
                            ingred4:"ketchup"
                            ingred4:"mustard"
                        ],
                }
        def post(self):
            userMeal = self.request.get("meal_choice")

            var_dict = {
                "meme_img_url": memeStringToUrl(userMeal)
            }
                results_template = the_jinja_env.get_template('templates/results.html')
                self.response.write(results_template.render(var_dict))

m1 = Meal("Burger",)

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        welcome_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(welcome_template.render())

class FoodInfoHandler(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('templates/Burgers.html')
        self.response.write(results_template.render())




app = webapp2.WSGIApplication([
    ('/',EnterInfoHandler ),
    ('/food',FoodInfoHandler)
], debug=True)
