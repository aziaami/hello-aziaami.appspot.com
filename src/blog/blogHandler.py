from google.appengine.ext import db

from src.BaseHandler import *
from src.blog.BlogDbEntry import *

class BlogHandler(BaseHandlerClass):
    def blogTemplate(self):
        return '/blog/newpost.html'

    def render_front(self, title="", blog="", error=""):                
        self.render(self.blogTemplate(), title=title, blog=blog, error=error)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get("title")
        blog = self.request.get("blog")

        if title and blog:
            b = BlogEntry(title = title, body = blog)
            b.put()
            self.redirect('/blog')

        else:
            error = "need both a title and a blog entry, please."
            self.render_front(title=title, blog=blog, error=error)