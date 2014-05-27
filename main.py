#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# editied by Aamir Aziz
# April 2014

from src.BaseHandler import *

from src.utils import dateVal

from src.unit2.rot13 import *
from src.unit2.jinja_test import *
from src.unit2.signup import *
from src.unit2.welcome import *

from src.blog.blogFrontHandler import *
from src.blog.blogHandler import *

import cgi 

def escape_html(s):
    return cgi.escape(s)

class MainHandler(BaseHandlerClass):
    def mainTemplate(self):
        return 'index.html'

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.render(self.mainTemplate())

    def post(self):
        d= escape_html(self.request.get('day'))
        m= escape_html(self.request.get('month'))
        y= escape_html(self.request.get('year'))

        if dateVal.valid_day(d) and dateVal.valid_month(m) and dateVal.valid_year(y):
            self.redirect('/thanks')
        else:
            error = "Incorrect. Please try again"
            self.render(self.mainTemplate(), error=error, d=d, m=m, y=y)



class ThanksHandler(BaseHandlerClass):
    def get(self):
        self.write("Thanks! Happy Birthday!")



class TestHandler(BaseHandlerClass):
    def get(self):
        q = self.request.get('q')
        self.write(q)
    
    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.write(self.request)



app = webapp2.WSGIApplication([
                ('/',                 MainHandler), 
                ('/testForm',         TestHandler),
                ('/thanks',           ThanksHandler),
                ('/unit2/rot13',      Rot13Handler),
                ('/unit2/jinja_test', JinjaTestHandler),
                ('/unit2/signup',     SignupHandler),
                ('/unit2/welcome',    WelcomeHandler),
                ('/blog',             BlogFrontHandler), 
                ('/blog/newpost',     BlogHandler)
      ], debug=True)