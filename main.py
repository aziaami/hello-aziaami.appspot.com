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
import webapp2
import cgi

from rot13 import *

page = """ 
aziaami search engine
<form action="http://www.google.com/search">
	<label> Google: <input name="q"> </label>
	<input type="submit">
</form>
<br> 
Print out request...
<form method="post" action="/testForm">
	<label> username: <input type="text" name="u"> 		</label>
	<label> password: <input type="password" name="q"> 	</label>
	<input type="submit">
</form>
<br>
What is your birthday ?
<form method="post">
	<label> Day   <input type="text" name="day" value="%(d)s">   </label>
	<label> Month <input type="text" name="month" value="%(m)s"> </label>
	<label> Year  <input type="text" name="year" value="%(y)s">  </label>
    <div style="color:red"> %(error)s </div>
	<br>
	<input type="submit">
</form>
<br>
<p>
Go to a page where you can <a href="/rot13">Rot13</a> your text.
</p>
"""

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


class MainHandler(webapp2.RequestHandler):
    def write_page(self, error="", d="", m="", y=""):
        self.response.out.write(page % {"error":error, "d":d, "m":m, "y":y})

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
    			('/',         MainHandler), 
    			('/testForm', TestHandler),
                ('/thanks',   ThanksHandler),
                ('/rot13',    Rot13Handler)
	  ], debug=True)