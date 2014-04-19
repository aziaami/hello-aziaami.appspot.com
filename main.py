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
import os
import webapp2
import jinja2
import cgi

from unit2.rot13 import *
from unit2.jinja_test import *


months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

def validate_day(day):
    if day and day.isdigit():
        day = int(day)
        if day in range(1,31):
            return day

def validate_month(month):
    if month:
        month = month.lower()
        month = month[0].upper() + month[1:]
        if (month in months):
            return month
        
def validate_year(year):
    if year and year.isdigit():
        year = int(year)
        if year in range(1900,2014):
            return year

def escape_html(s):
    return cgi.escape(s, quote=True)


jinja_env = jinja2.Environment(
                autoescape = True,
                loader = jinja2.FileSystemLoader(
                                    os.path.join(
                                        os.path.dirname(__file__),
                                        'templates')
                                    )
                )

class MainHandler(webapp2.RequestHandler):
    def write_page(self, error="", d="", m="", y=""):
        
        template_values = {
            "error":error, 
            "d":d, 
            "m":m, 
            "y":y }

        template = jinja_env.get_template('index.html')

        self.response.out.write(template.render(template_values))


    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_page()


    def post(self):
        d= self.request.get('day')
        m= self.request.get('month')
        y= self.request.get('year')

        validDay   = validate_day(d)
        validMonth = validate_month(m)
        validYear  = validate_year(y)

        if validDay and validMonth and validYear:
            self.redirect('/thanks')
        else:
            self.write_page(
                "Incorrect. Please try again", 
                escape_html(d),
                escape_html(m), 
                escape_html(y))


class TestHandler(webapp2.RequestHandler):
    def get(self):
        q = self.request.get('q')
        self.response.out.write(q)
    
    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(self.request)


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! Happy Birthday!")


app = webapp2.WSGIApplication([
    			('/',               MainHandler), 
    			('/testForm',       TestHandler),
                ('/thanks',         ThanksHandler),
                ('/unit2/rot13',    Rot13Handler),
                ('/unit2/jinja_test', JinjaTestHandler)
	  ], debug=True)