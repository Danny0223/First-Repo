import webapp2
import jinja2
import os
import models
from models import Food_Meal

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

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


#DISPLAY TOOL
class ViewHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/view_all_meals.html')
        self.response.write(result_template.render())

    def post(self):
        Choose_Your_Meal = self.request.get("Meal")
        #ContentName = self.request.get("CName")
        #AuthorName = self.request.get("AName")

        var_dict = {
            "Meal": Choose_Your_Meal
            #"CName": ContentName,
            #"AName": AuthorName
        }
        meal1= Food_Meal(name = Choose_Your_Meal)
        meal1.put()

        result_template = the_jinja_env.get_template('templates/view_all_meals.html')
        self.response.write(result_template.render(var_dict))

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/Results', ResultsPageHandler)

], debug=True)
