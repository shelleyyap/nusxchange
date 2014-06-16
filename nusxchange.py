import urllib
import webapp2
import jinja2
import os
import datetime

from google.appengine.ext import ndb
from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

# This part for the front page
class MainPage(webapp2.RequestHandler):
    # Handler for the front page.

    def get(self):
        template = jinja_environment.get_template('front.html')
        self.response.out.write(template.render())

class About(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render())

class Contact(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('contact.html')
        self.response.out.write(template.render())

class Countries(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('countries.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([('/', MainPage),
								('/about', About),
								('/contact', Contact),
                                ('/countries', Countries)],
                              debug=True)

