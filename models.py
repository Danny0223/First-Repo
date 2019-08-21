from google.appengine.ext import ndb

class BlogPost(ndb.Model):
    title = ndb.StringProperty(required=True)
    content = ndb.StringProperty(required=True)
    Name = ndb.StringProperty(required=True)
    #def autoplay(self):
