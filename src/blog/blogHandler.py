from src.BaseHandler import *

class BlogHandler(BaseHandlerClass):
    def get(self):
        self.write("this works")