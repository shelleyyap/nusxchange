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
      if users.get_current_user():
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url(self.request.host_url)
        }
      else:
        template_values = {
          'text': 'Login',
          'url':'/_ah/login_required'
        }
      template = jinja_environment.get_template('front.html')
      self.response.out.write(template.render(template_values))

class About(webapp2.RequestHandler):
    def get(self):
      if users.get_current_user():
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url(self.request.host_url)
        }
      else:
        template_values = {
          'text': 'Login',
          'url':'/_ah/login_required'
        }

      template = jinja_environment.get_template('about.html')
      self.response.out.write(template.render(template_values))

class Contact(webapp2.RequestHandler):
    def get(self):
      if users.get_current_user():
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url(self.request.host_url)
        }
      else:
        template_values = {
          'text': 'Login',
          'url':'/_ah/login_required'
        }
      template = jinja_environment.get_template('contact.html')
      self.response.out.write(template.render(template_values))

class Countries(webapp2.RequestHandler):
    def get(self):
      if users.get_current_user():
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url(self.request.host_url)
        }
      else:
        template_values = {
          'text': 'Login',
          'url':'/_ah/login_required'
        }
      template = jinja_environment.get_template('countries.html')
      self.response.out.write(template.render(template_values))

class Comments(ndb.Model):
  """Models an individual guestbook entry with author, content, and date."""
  author = ndb.UserProperty()
  content = ndb.StringProperty()
  date = ndb.DateTimeProperty(auto_now_add=True)

  @classmethod
  def query_book(cls, ancestor_key):
    return cls.query(ancestor=ancestor_key).order(-cls.date)

class School(ndb.Model):
  """Models an SEP partner university with general information, ratings, reviews and comments."""
  country = ndb.StringProperty()
  state = ndb.StringProperty()
  school_name = ndb.StringProperty()
  school_name_short = ndb.StringProperty()
  exchange_type = ndb.StringProperty()
  academic_calendar = ndb.StringProperty()

class Review(ndb.Model):
  """Models a review with author, date, major, university, date of exchange, ratings, review"""
  """Author details"""
  author = ndb.UserProperty()
  date = ndb.DateProperty(auto_now_add=True)
  semester = ndb.StringProperty()
  major = ndb.StringProperty()
  """Ratings"""
  overall_rating = ndb.IntegerProperty()
  cost_rating = ndb.IntegerProperty()
  life_rating = ndb.IntegerProperty()
  academics_rating = ndb.IntegerProperty()
  """Expenses"""
  total_expenditure = ndb.IntegerProperty()
  accommodation = ndb.IntegerProperty()
  food = ndb.IntegerProperty()
  transport = ndb.IntegerProperty()
  academic_needs = ndb.IntegerProperty()
  others = ndb.IntegerProperty()
  """Actual review"""
  content = ndb.TextProperty()

  @classmethod
  def query_review(cls, ancestor_key):
    return cls.query(ancestor=ancestor_key)

class Mapping(ndb.Model):
  """Models approved module mapping for a review"""
  exchange_module = ndb.StringProperty()
  credits = ndb.IntegerProperty()
  nus_module = ndb.StringProperty()
  nus_credits = ndb.IntegerProperty()

  @classmethod
  def query_mapping(cls, ancestor_key):
    return cls.query(ancestor=ancestor_key)

class GetSchool(webapp2.RequestHandler):
    def show(self):
        australia = School(country='Australia', state='Australia', school_name='ANU')
        australia.put()

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

        target = self.request.get('school')
        query = School.query(School.school_name.IN([target])).get()
        template_values = {
            'comments': comments,
            'url': url,
            'url_linktext': url_linktext,
            'school': query,
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
        
class University(webapp2.RequestHandler):
    def show(self):
        australia = School(country='Australia', state='Australia', school_name='ANU')
        australia.put()
        aus = School(country='Aus', state='Aus', school_name='aus')
        aus.put()
        target = self.request.get('school')
        query = School.query(School.school_name.IN([target])).get()

        comments_name = self.request.get('comments_name')
        # There is no need to actually create the parent Book entity; we can
        # set it to be the parent of another entity without explicitly creating it
        ancestor_key = ndb.Key("School", comments_name or "*notitle*")
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
            'school': query
        }

        template = jinja_environment.get_template('university.html')
        self.response.out.write(template.render(template_values))
    def get(self):
        self.show()
    def post(self):
        # Set parent key on each greeting to ensure that each
        # guestbook's greetings are in the same entity group.
        target = self.request.get('school')
        comments_name = self.request.get('comments_name')
        # There is no need to actually create the parent Book entity; we can
        # set it to be the parent of another entity without explicitly creating it
        comments = Comments(parent=ndb.Key("School", comments_name or "*notitle*"),
                            content = self.request.get('content'))
        if users.get_current_user():
            comments.author = users.get_current_user()
        comments.put()
        self.show()

        """Review"""
        reviews_name = self.request.get('reviews_name')
        review = Review(parent=ndb.Key("Book", reviews_name or "*notitle*"))
        review.author = '??'
        review.major = self.request.get('major')
        review.semester = self.request.get('sem')
        review.school = self.request.get('school') 
        review.overall_rating = self.request.get('overall')
        review.cost_rating = self.request.get('cost')
        review.life_rating = self.request.get('life')
        review.academics_rating = self.request.get('academics')
        review.total_expenditure = self.request.get('totalcost')
        review.accommodation = self.request.get('accomcost')
        review.food = self.request.get('foodcost')
        review.transport = self.request.get('transportcost')
        review.academic_needs = self.request.get('acadcost')
        review.others = self.request.get('othercost')
        review.content = self.request.get('reviewcontents')
        review.put()

        self.show()

class ToSubmitReview(webapp2.RequestHandler):
  def get(self):
    schools = School.query().get()
    template_values = {
      'author': 'name here',
      'schools': schools
    }
    template = jinja_environment.get_template('submitreview.html')
    self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage),
                                ('/about', About),
                                ('/contact', Contact),
                                ('/countries', Countries),
                                ('/university', University),
                                ('/getschool', GetSchool),
                                ('/tosubmitreview', ToSubmitReview)],
<<<<<<< HEAD
                              debug=True)
=======
                              debug=True)
>>>>>>> origin/master
