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
          'url': users.create_logout_url('about')
        }
      else:
        template_values = {
          'text': 'Login',
          'url':'/_ah/login_required?continue_url=about'
        }

      template = jinja_environment.get_template('about.html')
      self.response.out.write(template.render(template_values))

class Contact(webapp2.RequestHandler):
    def get(self):
      if users.get_current_user():
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url('/contact')
        }
      else:
        template_values = {
          'text': 'Login',
          'url':'/_ah/login_required?continue_url=contact'
        }
      template = jinja_environment.get_template('contact.html')
      self.response.out.write(template.render(template_values))

'''class Countries(webapp2.RequestHandler):
    def get(self):
      if users.get_current_user():
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url('/countries')
        }
      else:
        template_values = {
          'text': 'Login',
          'url':'/_ah/login_required?continue_url=/countries'
        }
      template = jinja_environment.get_template('countries.html')
      self.response.out.write(template.render(template_values))'''

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
  recommended_fac = ndb.StringProperty(repeated=True)
  mod_offered = ndb.StringProperty() # a url

  overall_rating = ndb.IntegerProperty()
  cost_rating = ndb.IntegerProperty()
  life_rating = ndb.IntegerProperty()
  academics_rating = ndb.IntegerProperty()

  total_expenditure = ndb.IntegerProperty()
  accomcost = ndb.IntegerProperty()
  foodcost = ndb.IntegerProperty()
  transportcost = ndb.IntegerProperty()
  academic_needs = ndb.IntegerProperty()
  othercost = ndb.IntegerProperty()

  content = ndb.TextProperty()
  #picture = ndb.StringProperty()

  @classmethod
  def query_country(cls, ancestor_key):
    return cls.query(ancestor=ancestor_key).order(-cls.date)


class Review(ndb.Model):
  """Models a review with author, date, major, university, date of exchange, ratings, review"""
  author = ndb.UserProperty()
  date = ndb.DateProperty(auto_now_add=True)
  year = ndb.GenericProperty()
  faculty = ndb.StringProperty()
  semester = ndb.StringProperty()
  major = ndb.StringProperty()

  overall_rating = ndb.IntegerProperty()
  cost_rating = ndb.IntegerProperty()
  life_rating = ndb.IntegerProperty()
  academics_rating = ndb.IntegerProperty()

  total_expenditure = ndb.GenericProperty()
  accommodation = ndb.GenericProperty()
  food = ndb.GenericProperty()
  transport = ndb.GenericProperty()
  academic_needs = ndb.GenericProperty()
  others = ndb.GenericProperty()

  content = ndb.TextProperty()

  @classmethod
  def query_review(cls, ancestor_key):
    return cls.query(ancestor=ancestor_key).order(-cls.date)


class University(webapp2.RequestHandler):
    def show(self):
        '''australia = School(country='Australia', state='Canberra', school_name='ANU')
        australia.put()
        aus = School(country='Aus', state='Aus', school_name='aus')
        aus.put()
        a = School(country='A', state='A', school_name='A', overall_rating=3)
        a.put()'''
        target = self.request.get('school')
        query = School.query(School.school_name_short.IN([target])).get()

        # There is no need to actually create the parent Book entity; we can
        # set it to be the parent of another entity without explicitly creating it
        ancestor_key = ndb.Key("School", target or "*notitle*")
        comments = Comments.query_book(ancestor_key).fetch()
        ancestor_key_review = ndb.Key("School", target or "*notitle*")
        reviews = Review.query_review(ancestor_key_review).fetch()

        # Displays the page. Used by both get and post
        if users.get_current_user():
            url = users.create_logout_url('/university?school=' + target)
            url_linktext = 'Logout'
        else:
            url = '/_ah/login_required?continue_url=/university?school=' + target
            url_linktext = 'Login'

        template_values = {
            'comments': comments,
            'url': url,
            'url_linktext': url_linktext,
            'school': query,
            'overall': 3, #temporary value
            'cost': 3, #temporary value
            'life': 3, #temporary value
            'academics': 3, #temporary value
            'total': 3, #temporary value
            'accommodation': 3, #temporary value
            'food': 3, #temporary value
            'transport': 3, #temporary value
            'academic_needs': 3, #temporary value
            'others': 3, #temporary value
            'reviews': reviews,
            'use': users.get_current_user(),
            'mod_offered': query.mod_offered
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


class ToSubmitReview(webapp2.RequestHandler):
  def get(self):
      target = self.request.get('school')
      query = School.query(School.school_name_short.IN([target])).get()
      template_values = {
          'text': 'Logout',
          'url': users.create_logout_url('/university?school=target'),
          'author': users.get_current_user(),
          'query': target
      }
      template = jinja_environment.get_template('submitreview.html')
      self.response.out.write(template.render(template_values))

class SubmittedReview(webapp2.RequestHandler):
  def post(self):
    reviews_name = self.request.get('reviews_name')
    review = Review(parent=ndb.Key("School", reviews_name or "*notitle*"))

    review.author = users.get_current_user()
    review.major = self.request.get('major')
    review.faculty = self.request.get('faculty') 
    review.year = self.request.get('year')
    review.semester = self.request.get('semester')

    review.overall_rating = int(self.request.get('overall'))
    review.cost_rating = int(self.request.get('cost'))
    review.life_rating = int(self.request.get('life'))
    review.academics_rating = int(self.request.get('academics'))

    review.total_expenditure = self.request.get('totalcost')
    review.accommodation = self.request.get('accomcost')
    review.food = self.request.get('foodcost')
    review.transport = self.request.get('transportcost')
    review.academic_needs = self.request.get('acadcost')
    review.others = self.request.get('othercost')
    review.content = self.request.get('reviewcontents')
    review.put()

    self.redirect("/university?school=" + reviews_name)

class DeleteReview(webapp2.RequestHandler):
  def get(self):
    
    review_school = self.request.get('school')

    #self.response.write('<html><body>You wrote:<pre>')
    #self.response.write(cgi.escape(self.request.get('school')))
    #self.response.write('</pre></body></html>')

    review_id = self.request.get('reviewid')
    review_key = ndb.Key(urlsafe=review_id)
    review_key.delete()

    

    self.redirect("/university?school=" + review_school)

class Countries(webapp2.RequestHandler):
    def get(self):
        #ndb.delete_multi(School.query().fetch(keys_only=True))
        #ndb.delete_multi(Review.query().fetch(keys_only=True))
        #ndb.delete_multi(Comments.query().fetch(keys_only=True))

        if users.get_current_user():
            template_values = {
                'text': 'Logout',
                'url': users.create_logout_url('/countries'),
                'countries': {'australia': "Australia", 'canada': "Canada", 'china': "China", 'germany': "Germany", 'hongkong': "Hong Kong"},
                'schools': {'australia':School.query(School.country == "Australia").fetch(), 'canada':School.query(School.country == "Canada").fetch(), 'china':School.query(School.country == "China").fetch(), 'germany':School.query(School.country == "Germany").fetch(), 'hongkong': School.query(School.country == "Hong Kong").fetch()}
            }
        else:
            template_values = {
            'text': 'Login',
            'url':'/_ah/login_required?continue_url=/countries',
            'countries': {'australia': "Australia", 'canada': "Canada", 'china': "China", 'germany': "Germany", 'hongkong': "Hong Kong"},
            'schools': {'australia':School.query(School.country == "Australia").fetch(), 'canada':School.query(School.country == "Canada").fetch(), 'china':School.query(School.country == "China").fetch(), 'germany':School.query(School.country == "Germany").fetch(), 'hongkong': School.query(School.country == "Hong Kong").fetch()}
            }

        template = jinja_environment.get_template('testcountries.html')
        self.response.out.write(template.render(template_values))

class AddUniversity(webapp2.RequestHandler):
    def get(self):
      countries_list={'australia': "Australia", 'canada': "Canada", 'china': "China", 'germany': "Germany", 'hongkong': "Hong Kong"}
      if users.get_current_user():
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url('/countries'),
        }
      else:
        template_values = {
          'text': 'Login',
          'url':'/_ah/login_required?continue_url=/countries'
        }
      template = jinja_environment.get_template('adduniversity.html')
      self.response.out.write(template.render(template_values))

class AddedUniversity(webapp2.RequestHandler):
  def post(self):
    #self.response.write('<html><body>You wrote:<pre>')
    #self.response.write(cgi.escape(self.request.get('name')))
    #self.response.write('</pre></body></html>')

    sch = School()
    sch.school_name=self.request.get('name')
    sch.school_name_short=self.request.get('short_name')
    sch.country=self.request.get('country')
    sch.state=self.request.get('state')
    sch.exchange_type=self.request.get('exchange_type')
    sch.academic_calendar=self.request.get('calendar')
    sch.recommended_fac=self.request.get_all('faculty')
    sch.mod_offered=self.request.get('modules')
    #sch.picture=self.request.get('img')
    sch.content=self.request.get('abtschool')    
    sch.put()
    self.redirect("/university?school=" + sch.school_name_short)


app = webapp2.WSGIApplication([('/', MainPage),
                                ('/about', About),
                                ('/contact', Contact),
                                ('/countries', Countries),
                                ('/university', University),
                                ('/tosubmitreview', ToSubmitReview),
                                ('/submittedreview', SubmittedReview),
                                ('/deletereview', DeleteReview),
                                ('/adduniversity', AddUniversity),
                                ('/addeduniversity', AddedUniversity)],
                              debug=True)
