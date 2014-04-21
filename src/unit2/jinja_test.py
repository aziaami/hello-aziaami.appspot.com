import os
import webapp2
import jinja2

jinja_env = jinja2.Environment(	
		autoescape=True,
		loader=jinja2.FileSystemLoader(
				os.path.join(
					os.path.dirname(__file__),
					'../templates/unit2')
				)
		)

class JinjaTestHandler(webapp2.RequestHandler):
    def get(self):
        template_vals = {
            'name':'aziaami',
            'verb':'enjoy'
        }
        
        template = jinja_env.get_template('jinja_test.html')
        self.response.out.write(
                template.render(template_vals))
