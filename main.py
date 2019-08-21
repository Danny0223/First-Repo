import webapp2
import jinja2
import os
import models
from models import BlogPost

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#MAIN PAGE WHERE USER IS FIRST AT

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(result_template.render())

class ResultPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(result_template.render())

"""
class BlogHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/new_post.html')
        self.response.write(result_template.render())
"""


class ViewHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/view_all_meals.html')
        self.response.write(result_template.render())

    def post(self):
        Choose Your Meal = self.request.get("Meal")
        #ContentName = self.request.get("CName")
        #AuthorName = self.request.get("AName")

        var_dict = {
            "Meal": Choose Your Meal,
            #"CName": ContentName,
            #"AName": AuthorName
        }
        meal1= Food_Meal(name = Choose Your Meal)
        meal1.put()

        result_template = the_jinja_env.get_template('templates/view_all_meals.html')
        self.response.write(result_template.render(var_dict))

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/Results', ResultsPageHandler),
    #('/blog',BlogHandler),
    ('/view_all_meals',ViewHandler)

], debug=True)
