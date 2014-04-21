import webapp2

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-type']='text/html'
        self.response.out.write("Welcome!")
