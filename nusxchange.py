import urllib
import cgi
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

class Comments(ndb.Model):
  """Models an individual guestbook entry with author, content, and date."""
  author = ndb.UserProperty()
  content = ndb.StringProperty()
  date = ndb.DateTimeProperty(auto_now_add=True)

  @classmethod
  def query_book(cls, ancestor_key):
    return cls.query(ancestor=ancestor_key).order(-cls.date)

class University(webapp2.RequestHandler):
    def show(self):
        comments_name = self.request.get('comments_name')
        # There is no need to actually create the parent Book entity; we can
        # set it to be the parent of another entity without explicitly creating it
        ancestor_key = ndb.Key("Book", comments_name or "*notitle*")
        comments = Comments.query_book(ancestor_key).fetch(20)
        # Displays the page. Used by both get and post
        if users.get_current_user():
            url = 'https://ivle.nus.edu.sg/api/login/?apikey=7265pvtX25EZZQkAOOCx1&url=http://localhost:8080/'
            url_linktext = 'Logout'
        else:
            url = 'https://ivle.nus.edu.sg/api/login/?apikey=7265pvtX25EZZQkAOOCx1&url=http://localhost:8080/'
            url_linktext = 'Login'
        template_values = {
            'comments': comments,
            'url': url,
            'url_linktext': url_linktext,
        }

        template = jinja_environment.get_template('university.html')
        self.response.out.write(template.render(template_values))
    def get(self):
        self.show()
    def post(self):
        # Set parent key on each greeting to ensure that each
        # guestbook's greetings are in the same entity group.
        comments_name = self.request.get('comments_name')
        # There is no need to actually create the parent Book entity; we can
        # set it to be the parent of another entity without explicitly creating it
        comments = Comments(parent=ndb.Key("Book", comments_name or "*notitle*"),
                            content = self.request.get('content'))
        if users.get_current_user():
            comments.author = users.get_current_user()
        comments.put()
        self.show()


app = webapp2.WSGIApplication([('/', MainPage),
                                ('/about', About),
                                ('/contact', Contact),
                                ('/countries', Countries),
                                ('/university', University)],
                              debug=True)
