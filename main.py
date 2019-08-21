import webapp2
import jinja2
import os
import models
from models import BlogPost

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(result_template.render())

class FamilyPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/about_my_family.html')
        self.response.write(result_template.render())

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/new_post.html')
        self.response.write(result_template.render())



class ViewHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/view_all_posts.html')
        self.response.write(result_template.render())

    def post(self):
        TitleName = self.request.get("TName")
        ContentName = self.request.get("CName")
        AuthorName = self.request.get("AName")

        var_dict = {
            "TName": TitleName,
            "CName": ContentName,
            "AName": AuthorName
        }
        blog1 = BlogPost(Name = AuthorName,title= TitleName,content= ContentName)
        blog1.put()

        result_template = the_jinja_env.get_template('templates/view_all_posts.html')
        self.response.write(result_template.render(var_dict))

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/about_my_family', FamilyPageHandler),
    ('/blog',BlogHandler),
    ('/view_all_posts',ViewHandler)

], debug=True)
