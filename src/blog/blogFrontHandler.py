from google.appengine.ext import db

from src.BaseHandler import *
from src.blog.BlogDbEntry import *

class BlogFrontHandler(BaseHandlerClass):
    def blogTemplate(self):
        return '/blog/front.html'

    def render_front(self):        
        blogEntries = db.GqlQuery("SELECT * FROM BlogEntry ORDER BY created DESC")
        self.render(self.blogTemplate(), blogEntries = blogEntries)

    def get(self):
        self.render_front()