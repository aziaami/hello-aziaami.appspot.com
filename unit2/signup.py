import os
import webapp2
import jinja2
import cgi
import re

jinja_env = jinja2.Environment(
                autoescape = True,
                loader = jinja2.FileSystemLoader(
                                    os.path.join(
                                        os.path.dirname(__file__),
                                        '../templates/unit2')
                                    )
                )

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


class SignupHandler(webapp2.RequestHandler):
    def write_page(self, user="", email="", user_err="", pw_err="", pw2_err="", em_error=""):
        
        template_values = {
            "username":user, 
            "email":email,
            "username_error":user_err, 
            "password_error":pw_err, 
            "password2_error":pw2_err,
            "email_error":em_error }

        template = jinja_env.get_template('signup.html')

        self.response.out.write(template.render(template_values))

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_page()

    def post(self):
        
        un = self.request.get("username")
        pw = self.request.get("password")
        pw2= self.request.get("password2")
        em = self.request.get("email")

        #validate inputs
        val_un = valid_username(cgi.escape(un))
        val_pw = valid_password(cgi.escape(pw))
        val_em = valid_email(cgi.escape(em))
        matching_pw = (cgi.escape(pw) == cgi.escape(pw2))
        
        if ( val_un and val_pw and val_em and matching_pw):
            #redirect to welcome page
            self.redirect('/unit2/welcome?username=' + un)            
        else:
            #self.response.out.write("Sorry , error...")
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
            
            self.write_page( un, 
                             em,
                             un_e,
                             pw_e,
                             pw2_e,
                             em_e)