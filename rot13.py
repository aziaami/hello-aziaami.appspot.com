import webapp2
import cgi

page = """
<!doctype html>
<html lang="en">
<head>
    <title> Rot13 </title>
</head>
<body>

    Enter text to Rot13 ...
    <form method="post">
        <textarea name="text" rows="4" cols="50">%(r)s
        </textarea>
        <br>
    	<input type=submit>
    </form>

</body>
</html>
"""

def make_dict():
    rotate13 = {}
    l_in  = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    l_rot = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    for idx, val in enumerate(l_in):
        rotate13[val] = l_rot[idx]
    return rotate13

def rot_13(s):
    rot_dict = make_dict()
    s_roted  = ""
    
    for let in s:
        if let in rot_dict:
            s_roted += rot_dict[let]
            continue
        s_roted += let

    return cgi.escape(s_roted)

class Rot13Handler(webapp2.RequestHandler):
    def write_page(self, r=""):
        self.response.out.write(page % {"r":r})

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_page()
            
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        text = self.request.get('text')
        self.write_page(rot_13(text))