import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        welcome_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(welcome_template.render())

class FoodInfoHandler(webapp2.RequestHandler):
    def get(self):





app = webapp2.WSGIApplication([
    ('/',EnterInfoHandler ),
    ('/danny',FoodInfoHandler)
], debug=True)
