from src.BaseHandler import *

import cgi
import re

#Regular Expressions to help check users, passwords and emails
USER_RE  = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE  = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")


def valid_username(username):
    return USER_RE.match(username)

def valid_password(pw):
    return PASS_RE.match(pw)

def valid_email(email):
    if email=="" or EMAIL_RE.match(email):
        return True

def escape_html(s):
    return cgi.escape(s)

class SignupHandler(BaseHandlerClass):
    def signupTemplate(self):
        return '/unit2/signup.html'

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.render(self.signupTemplate())

    def post(self):        
        un = escape_html(self.request.get("username"))
        pw = escape_html(self.request.get("password"))
        pw2= escape_html(self.request.get("password2"))
        em = escape_html(self.request.get("email"))
        
        val_un = valid_username(un)
        val_pw = valid_password(pw)
        val_em = valid_email(em)
        matching_pw = (pw == pw2)
        
        if ( val_un and val_pw and val_em and matching_pw):            
            self.redirect('/unit2/welcome?username=' + un)            
        else:            
            un_e  = ""
            pw_e  = ""
            pw2_e = ""
            em_e  = ""

            if not val_un:
                un_e  = "invalid username"
            if not val_pw:
                pw_e  = "invaild password"
            if not matching_pw:
                pw2_e = "passwords don't match"
            if not val_em:
                em_e = "invalid email"
            
            template_values = {
                    "username":un, 
                    "email":em,
                    "username_error":un_e, 
                    "password_error":pw_e, 
                    "password2_error":pw2_e,
                    "email_error":em_e }

            self.render(self.signupTemplate(), **template_values)