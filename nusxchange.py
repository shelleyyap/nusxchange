import sys
sys.path.insert(0, 'libs')
import urllib
import cgi
import webapp2
import jinja2
import os
import datetime
import re
import quopri

from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import images
from bs4 import BeautifulSoup, Comment
from urlparse import urljoin
from google.appengine.api import search
import logging



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

# This part for the front page
class MainPage(webapp2.RequestHandler):
    # Handler for the front page.
    def get(self):
      if users.is_current_user_admin():
        template_values = {
          'text': 'Logout',
          'url' : users.create_logout_url(self.request.host_url)
        }
        template = jinja_environment.get_template('frontadmin.html')
        self.response.out.write(template.render(template_values))
      elif users.get_current_user():
        if users.get_current_user().email().find('nus') > 0: # NUS account.  
          template_values = {
              'text': 'Logout',
              'url': users.create_logout_url(self.request.host_url),
          }
          template = jinja_environment.get_template('frontuser.html')
          self.response.out.write(template.render(template_values))
        else: #Not NUS account. Means no permission
          template_values = {
            'errormsg': 'gmail',
            'redirectlink': users.create_logout_url(self.request.host_url)
          }
          template = jinja_environment.get_template('loginerror.html')
          self.response.out.write(template.render(template_values))
      else:
        template_values = {
          'text': 'NUS Login',
          'url':'/_ah/login_required',
          'admintext': 'Admin Login',
          'adminurl': '/_ah/login_required?continue_url=/login'
        }
        template = jinja_environment.get_template('front.html')
        self.response.out.write(template.render(template_values))

class Login(webapp2.RequestHandler):
  def get(self):
      if users.is_current_user_admin():
        template_values = {
          'text': 'Logout',
          'url' : users.create_logout_url(self.request.host_url)
        }
        template = jinja_environment.get_template('frontadmin.html')
        self.response.out.write(template.render(template_values))
      else:
        template_values = {
          'redirectlink': users.create_logout_url(self.request.host_url)
        }
        template = jinja_environment.get_template('loginerror.html')
        self.response.out.write(template.render(template_values))



class About(webapp2.RequestHandler):
    def get(self):
      if users.is_current_user_admin():
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url('/about')
        }
        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render(template_values))
      elif users.get_current_user():
        if users.get_current_user().email().find('nus') > 0: # NUS account. 
          template_values = {
            'text': 'Logout',
            'url': users.create_logout_url('/about')
          }
          template = jinja_environment.get_template('about.html')
          self.response.out.write(template.render(template_values))
        else: #Not NUS account. Means no permission
          template_values = {
            'errormsg': 'gmail',
            'redirectlink': users.create_logout_url('/about')
          }
          template = jinja_environment.get_template('loginerror.html')
          self.response.out.write(template.render(template_values))
      else:
        template_values = {
          'text': 'Login',
          'url':'/_ah/login_required?continue_url=/about'
        }

        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render(template_values))

class Contact(webapp2.RequestHandler):
    def get(self):
      if users.is_current_user_admin():
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url('/contact')
        }
        template = jinja_environment.get_template('contact.html')
        self.response.out.write(template.render(template_values))
      elif users.get_current_user():
        if users.get_current_user().email().find('nus') > 0: # NUS account. 
          template_values = {
            'text': 'Logout',
            'url': users.create_logout_url('/contact')
          }
          template = jinja_environment.get_template('contact.html')
          self.response.out.write(template.render(template_values))
        else: #Not NUS account. Means no permission
          template_values = {
            'errormsg': 'gmail',
            'redirectlink': users.create_logout_url('/contact')
          }
          template = jinja_environment.get_template('loginerror.html')
          self.response.out.write(template.render(template_values))
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

class Mapping(ndb.Model):
  sep_mod = ndb.StringProperty()
  sep_mc = ndb.IntegerProperty()
  nus_mod = ndb.StringProperty()
  nus_mc = ndb.IntegerProperty()
  map_id = ndb.IntegerProperty()

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
  mod_mappings = ndb.StructuredProperty(Mapping, repeated=True)

  overall_rating = ndb.FloatProperty()
  cost_rating = ndb.FloatProperty()
  life_rating = ndb.FloatProperty()
  academics_rating = ndb.FloatProperty()

  total_expenditure = ndb.IntegerProperty()
  accomcost = ndb.IntegerProperty()
  foodcost = ndb.IntegerProperty()
  transportcost = ndb.IntegerProperty()
  academic_needs = ndb.IntegerProperty()
  othercost = ndb.IntegerProperty()

  content = ndb.TextProperty()
  picture = ndb.BlobKeyProperty()
  num_reviews = ndb.IntegerProperty()
  mappings_count = ndb.IntegerProperty()

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

  total_expenditure = ndb.IntegerProperty()
  accommodation = ndb.IntegerProperty()
  food = ndb.IntegerProperty()
  transport = ndb.IntegerProperty()
  academic_needs = ndb.IntegerProperty()
  others = ndb.IntegerProperty()

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
        if users.is_current_user_admin():
            url = users.create_logout_url('/university?school=' + target)
            url_linktext = 'Logout'
            img_url = images.get_serving_url(query.picture)
            template_values = {
                'comments': comments,
                'url': url,
                'url_linktext': url_linktext,
                'school': query,
                'pic': img_url,
                'overall': round(query.overall_rating,1), #temporary value
                'cost': round(query.cost_rating,1), #temporary value
                'life': round(query.life_rating,1), #temporary value
                'academics': round(query.academics_rating,1), #temporary value
                'total': query.total_expenditure, #temporary value
                'accommodation': query.accomcost, #temporary value
                'food': query.foodcost, #temporary value
                'transport': query.transportcost, #temporary value
                'academic_needs': query.academic_needs, #temporary value
                'others': query.othercost, #temporary value
                'reviews': reviews,
                'use': users.get_current_user(),
                'mod_offered': query.mod_offered,
                'admin': users.is_current_user_admin()
            }

            template = jinja_environment.get_template('university.html')
            self.response.out.write(template.render(template_values))
        elif users.get_current_user(): 
          if users.get_current_user().email().find('nus') > 0: # NUS account. 
            url = users.create_logout_url('/university?school=' + target)
            url_linktext = 'Logout'
            img_url = images.get_serving_url(query.picture)
            template_values = {
                'comments': comments,
                'url': url,
                'url_linktext': url_linktext,
                'school': query,
                'pic': img_url,
                'overall': round(query.overall_rating,1), #temporary value
                'cost': round(query.cost_rating,1), #temporary value
                'life': round(query.life_rating,1), #temporary value
                'academics': round(query.academics_rating,1), #temporary value
                'total': query.total_expenditure, #temporary value
                'accommodation': query.accomcost, #temporary value
                'food': query.foodcost, #temporary value
                'transport': query.transportcost, #temporary value
                'academic_needs': query.academic_needs, #temporary value
                'others': query.othercost, #temporary value
                'reviews': reviews,
                'use': users.get_current_user(),
                'mod_offered': query.mod_offered,
                'admin': users.is_current_user_admin()
            }

            template = jinja_environment.get_template('university.html')
            self.response.out.write(template.render(template_values))
          else: #Not NUS account. Means no permission
            template_values = {
              'errormsg': 'gmail',
              'redirectlink': users.create_logout_url('/university?school=' + target)
            }
            template = jinja_environment.get_template('loginerror.html')
            self.response.out.write(template.render(template_values))
        else:
            url = '/_ah/login_required?continue_url=/university?school=' + target
            url_linktext = 'Login'

            img_url = images.get_serving_url(query.picture)
            template_values = {
                'comments': comments,
                'url': url,
                'url_linktext': url_linktext,
                'school': query,
                'pic': img_url,
                'overall': round(query.overall_rating,1), #temporary value
                'cost': round(query.cost_rating,1), #temporary value
                'life': round(query.life_rating,1), #temporary value
                'academics': round(query.academics_rating,1), #temporary value
                'total': query.total_expenditure, #temporary value
                'accommodation': query.accomcost, #temporary value
                'food': query.foodcost, #temporary value
                'transport': query.transportcost, #temporary value
                'academic_needs': query.academic_needs, #temporary value
                'others': query.othercost, #temporary value
                'reviews': reviews,
                'use': users.get_current_user(),
                'mod_offered': query.mod_offered,
                'admin': users.is_current_user_admin()
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
      if users.is_current_user_admin():
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url('/university?school=' + target),
          'author': users.get_current_user(),
          'query': target,
          'upload_url': blobstore.create_upload_url('/submittedreview')
        }
        template = jinja_environment.get_template('submitreview.html')
        self.response.out.write(template.render(template_values))
      elif users.get_current_user():
        if users.get_current_user().email().find('nus') > 0: # NUS account. 
          template_values = {
            'text': 'Logout',
            'url': users.create_logout_url('/university?school=' + target),
            'author': users.get_current_user(),
            'query': target,
            'upload_url': blobstore.create_upload_url('/submittedreview')
          }
          template = jinja_environment.get_template('submitreview.html')
          self.response.out.write(template.render(template_values))
        else: #Not NUS account. Means no permission
            template_values = {
              'errormsg': 'gmail',
              'redirectlink': users.create_logout_url('/university?school=' + target)
            }
            template = jinja_environment.get_template('loginerror.html')
            self.response.out.write(template.render(template_values))
      else:
            template_values = {
              'errormsg': 'gmail',
              'redirectlink': users.create_logout_url('/university?school=' + target)
            }
            template = jinja_environment.get_template('loginerror.html')
            self.response.out.write(template.render(template_values))

class SubmittedReview(webapp2.RequestHandler):
  def post(self):
    def sanitizeHtml(value, base_url=None):
      rjs = r'[\s]*(&#x.{1,7})?'.join(list('javascript:'))
      rvb = r'[\s]*(&#x.{1,7})?'.join(list('vbscript:'))
      re_scripts = re.compile('(%s)|(%s)' % (rjs, rvb), re.IGNORECASE)
      validTags = 'p i strong b u a h1 h2 h3 pre br img'.split()
      validAttrs = 'href src width height'.split()
      urlAttrs = 'href src'.split() # Attributes which should have a URL
      soup = BeautifulSoup(value)
      for comment in soup.findAll(text=lambda text: isinstance(text, Comment)):
        # Get rid of comments
        comment.extract()
      for tag in soup.findAll(True):
        if tag.name not in validTags:
          tag.hidden = True
        attrs = tag.attrs
        tag.attrs = []
        for attr, val in attrs:
          if attr in validAttrs:
            val = re_scripts.sub('', val) # Remove scripts (vbs & js)
            if attr in urlAttrs:
              val = urljoin(base_url, val) # Calculate the absolute url
            tag.attrs.append((attr, val))
      return soup.renderContents().decode('utf8')

    reviews_name = self.request.get('reviews_name')
    review = Review(parent=ndb.Key("School", reviews_name or "*notitle*"))
    query = School.query(School.school_name_short.IN([reviews_name])).get()

    review.author = users.get_current_user()
    review.major = self.request.get('major')
    review.faculty = self.request.get('faculty') 
    review.year = self.request.get('year')
    review.semester = self.request.get('semester')

    num = query.num_reviews
    review.overall_rating = int(self.request.get('overall'))
    query.overall_rating = (query.overall_rating * num + review.overall_rating)/(num + 1.0)
    review.cost_rating = int(self.request.get('cost'))
    query.cost_rating = (query.cost_rating * num + review.cost_rating)/(num + 1.0)
    review.life_rating = int(self.request.get('life'))
    query.life_rating = (query.life_rating * num + review.life_rating)/(num + 1.0)
    review.academics_rating = int(self.request.get('academics'))
    query.academics_rating = (query.academics_rating * num + review.academics_rating)/(num + 1.0)
    review.accommodation = int(self.request.get('accomcost'))
    query.accomcost = int((query.accomcost * num + review.accommodation)/(num + 1))
    review.food = int(self.request.get('foodcost'))
    query.foodcost = int((query.foodcost * num + review.food)/(num + 1))
    review.transport = int(self.request.get('transportcost'))
    query.transportcost = int((query.transportcost * num + review.transport)/(num + 1))
    review.academic_needs = int(self.request.get('acadcost'))
    query.academic_needs = int((query.academic_needs * num + review.academic_needs)/(num + 1))
    review.others = int(self.request.get('othercost'))
    query.othercost = int((query.othercost * num + review.others)/(num + 1))
    review.total_expenditure = int(review.accommodation + review.food + review.transport + review.academic_needs + review.others)
    query.total_expenditure = int((query.total_expenditure * num + review.total_expenditure)/(num + 1))
    review.content = sanitizeHtml(self.request.get('reviewcontents'))
    
    index=search.Index(name="my_index3")
    
    my_document = search.Document(
      doc_id = query.school_name_short,
      fields=[
        search.TextField(name='name', value=query.school_name),
        search.TextField(name='short_name', value=query.school_name_short),
        search.AtomField(name='country', value=query.country),
        search.AtomField(name='state', value=query.state),
        search.TextField(name='exchange_type', value=query.exchange_type),
        search.TextField(name='calendar', value=query.academic_calendar),
        search.TextField(name='faculty',value=review.faculty),
        search.TextField(name='about',value=query.content),
        search.NumberField(name='overall_rating', value=query.overall_rating),
        search.NumberField(name='cost_rating',value=query.cost_rating),
        search.NumberField(name='life_rating',value=query.life_rating),
        search.NumberField(name='academics_rating',value=query.academics_rating),
        search.NumberField(name='total_expenditure',value=query.total_expenditure),
        search.NumberField(name='accomcost',value=query.accomcost),
        search.NumberField(name='foodcost',value=query.foodcost),
        search.NumberField(name='transportcost',value=query.transportcost),
        search.NumberField(name='academic_needs',value=query.academic_needs),
        search.NumberField(name='othercost',value=query.othercost)])
    
    try:
      index.put(my_document)
    except search.PutError, e:
      logging.exception("Add failed")

    query.num_reviews = query.num_reviews + 1
    count = query.mappings_count

    if self.request.get('mod1') != '':
      mod1 = Mapping()
      mod1.sep_mod = self.request.get('mod1')
      mod1.sep_mc = int(self.request.get('cred1'))
      mod1.nus_mod = self.request.get('nmod1')
      mod1.nus_mc = int(self.request.get('mc1'))
      mod1.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod1)

    if self.request.get('mod2') != '':
      mod2 = Mapping()
      mod2.sep_mod = self.request.get('mod2')
      mod2.sep_mc = int(self.request.get('cred2'))
      mod2.nus_mod = self.request.get('nmod2')
      mod2.nus_mc = int(self.request.get('mc2'))
      mod2.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod2)

    if self.request.get('mod3') != '':
      mod3 = Mapping()
      mod3.sep_mod = self.request.get('mod3')
      mod3.sep_mc = int(self.request.get('cred3'))
      mod3.nus_mod = self.request.get('nmod3')
      mod3.nus_mc = int(self.request.get('mc3'))
      mod3.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod3)

    if self.request.get('mod4') != '':
      mod4 = Mapping()
      mod4.sep_mod = self.request.get('mod4')
      mod4.sep_mc = int(self.request.get('cred4'))
      mod4.nus_mod = self.request.get('nmod4')
      mod4.nus_mc = int(self.request.get('mc4'))
      mod4.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod4)

    if self.request.get('mod5') != '':
      mod5 = Mapping()
      mod5.sep_mod = self.request.get('mod5')
      mod5.sep_mc = int(self.request.get('cred5'))
      mod5.nus_mod = self.request.get('nmod5')
      mod5.nus_mc = int(self.request.get('mc5'))
      mod5.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod5)

    if self.request.get('mod6') != '':
      mod6 = Mapping()
      mod6.sep_mod = self.request.get('mod6')
      mod6.sep_mc = int(self.request.get('cred6'))
      mod6.nus_mod = self.request.get('nmod6')
      mod6.nus_mc = int(self.request.get('mc6'))
      mod6.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod6)

    if self.request.get('mod7') != '':
      mod7 = Mapping()
      mod7.sep_mod = self.request.get('mod7')
      mod7.sep_mc = int(self.request.get('cred7'))
      mod7.nus_mod = self.request.get('nmod7')
      mod7.nus_mc = int(self.request.get('mc7'))
      mod7.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod7)

    if self.request.get('mod8') != '':
      mod8 = Mapping()
      mod8.sep_mod = self.request.get('mod8')
      mod8.sep_mc = int(self.request.get('cred8'))
      mod8.nus_mod = self.request.get('nmod8')
      mod8.nus_mc = int(self.request.get('mc8'))
      mod8.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod8)

    if self.request.get('mod9') != '':
      mod9 = Mapping()
      mod9.sep_mod = self.request.get('mod9')
      mod9.sep_mc = int(self.request.get('cred9'))
      mod9.nus_mod = self.request.get('nmod9')
      mod9.nus_mc = int(self.request.get('mc9'))
      mod9.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod9)

    if self.request.get('mod10') != '':
      mod10 = Mapping()
      mod10.sep_mod = self.request.get('mod10')
      mod10.sep_mc = int(self.request.get('cred10'))
      mod10.nus_mod = self.request.get('nmod10')
      mod10.nus_mc = int(self.request.get('mc10'))
      mod10.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod10)

    query.mappings_count = count
    query.put()
    review.put()

    self.redirect("/university?school=" + reviews_name)

class DeleteReview(webapp2.RequestHandler):
  def get(self):
    
    review_school = self.request.get('school')
    query = School.query(School.school_name_short.IN([review_school])).get()
    num = query.num_reviews

    review_id = self.request.get('reviewid')
    review_key = ndb.Key(urlsafe=review_id)
    review = review_key.get()

    if ((num - 1) == 0):
      query.overall_rating=0
      query.cost_rating=0
      query.life_rating=0
      query.academics_rating=0
      query.accomcost=0
      query.foodcost=0
      query.transportcost=0
      query.academic_needs=0
      query.othercost=0
      query.total_expenditure = 0
    else:
      overall = review.overall_rating
      query.overall_rating = (query.overall_rating * (num) - overall)/(num - 1)
      cost = review.cost_rating
      query.cost_rating = ((query.cost_rating) * (num) - cost)/(num - 1)
      life = review.life_rating
      query.life_rating = ((query.life_rating) * (num) - life)/(num - 1)
      academics = review.academics_rating
      query.academics_rating = ((query.academics_rating) * (num) - academics)/(num - 1)

      accom = review.accommodation
      query.accomcost = (query.accomcost * num - accom)/(num - 1)
      food = review.food 
      query.foodcost = (query.foodcost * num - food)/(num - 1)
      transport = review.transport
      query.transportcost = (query.transportcost * num - transport)/(num - 1)
      academic_needs = review.academic_needs
      query.academic_needs = (query.academic_needs * num - academic_needs)/(num - 1)
      others = review.others
      query.othercost = (query.othercost * num - others)/(num - 1)
      query.total_expenditure = (query.total_expenditure * num - accom - food - transport - academic_needs - others)/(num - 1)

    index=search.Index(name="my_index3")
    
    my_document = search.Document(
      doc_id = query.school_name_short,
      fields=[
        search.TextField(name='name', value=query.school_name),
        search.TextField(name='short_name', value=query.school_name_short),
        search.AtomField(name='country', value=query.country),
        search.AtomField(name='state', value=query.state),
        search.TextField(name='exchange_type', value=query.exchange_type),
        search.TextField(name='calendar', value=query.academic_calendar),
        search.TextField(name='faculty',value=review.faculty),
        search.TextField(name='about',value=query.content),
        search.NumberField(name='overall_rating', value=query.overall_rating),
        search.NumberField(name='cost_rating',value=query.cost_rating),
        search.NumberField(name='life_rating',value=query.life_rating),
        search.NumberField(name='academics_rating',value=query.academics_rating),
        search.NumberField(name='total_expenditure',value=query.total_expenditure),
        search.NumberField(name='accomcost',value=query.accomcost),
        search.NumberField(name='foodcost',value=query.foodcost),
        search.NumberField(name='transportcost',value=query.transportcost),
        search.NumberField(name='academic_needs',value=query.academic_needs),
        search.NumberField(name='othercost',value=query.othercost)])
    
    try:
      index.put(my_document)
    except search.PutError, e:
      logging.exception("Add failed")

    query.num_reviews = query.num_reviews - 1
    query.put()
    review_key.delete()
    self.redirect("/university?school=" + review_school)

class DeleteComment(webapp2.RequestHandler):
  def get(self):
    
    comment_school = self.request.get('school')

    #self.response.write('<html><body>You wrote:<pre>')
    #self.response.write(cgi.escape(self.request.get('school')))
    #self.response.write('</pre></body></html>')

    comment_id = self.request.get('commentid')
    comment_key = ndb.Key(urlsafe=comment_id)
    comment_key.delete()

    self.redirect("/university?school=" + comment_school)

class Countries(webapp2.RequestHandler):
    def get(self):
        # To delete all data
        #ndb.delete_multi(School.query().fetch(keys_only=True))
        #ndb.delete_multi(Review.query().fetch(keys_only=True))
        #ndb.delete_multi(Comments.query().fetch(keys_only=True))

        if users.is_current_user_admin():
            template_values = {
                'text': 'Logout',
                'url': users.create_logout_url('/countries'),
                'admin': users.is_current_user_admin(),
                'anocountries': ['australia', 'canada', 'china', 'germany', 'hongkong', 'newzealand', 'southkorea', 'sweden', 'usa'],
                'countries': {'china': "China", 'australia': "Australia", 'germany': "Germany", 'canada': "Canada",'hongkong': "Hong Kong", 'newzealand': 'New Zealand', 'southkorea': 'South Korea', 'sweden': 'Sweden', 'usa': 'United States of America'},
                'schools': {'australia':School.query(School.country == "Australia").fetch(), 'canada':School.query(School.country == "Canada").fetch(), 'china':School.query(School.country == "China").fetch(), 'germany':School.query(School.country == "Germany").fetch(), 'hongkong': School.query(School.country == "HongKong").fetch(), 'newzealand': School.query(School.country == "NewZealand").fetch(), 'southkorea': School.query(School.country == "SouthKorea").fetch(), 'sweden': School.query(School.country == "Sweden").fetch(), 'usa': School.query(School.country == "USA").fetch()}
            }
            template = jinja_environment.get_template('testcountries.html')
            self.response.out.write(template.render(template_values))

        elif users.get_current_user():
          if users.get_current_user().email().find('nus') > 0: # NUS account. 
            template_values = {
                'text': 'Logout',
                'url': users.create_logout_url('/countries'),
                'admin': users.is_current_user_admin(),
                'anocountries': ['australia', 'canada', 'china', 'germany', 'hongkong', 'newzealand', 'southkorea', 'sweden', 'usa'],
                'countries': {'china': "China", 'australia': "Australia", 'germany': "Germany", 'canada': "Canada",'hongkong': "Hong Kong", 'newzealand': 'New Zealand', 'southkorea': 'South Korea', 'sweden': 'Sweden', 'usa': 'United States of America'},
                'schools': {'australia':School.query(School.country == "Australia").fetch(), 'canada':School.query(School.country == "Canada").fetch(), 'china':School.query(School.country == "China").fetch(), 'germany':School.query(School.country == "Germany").fetch(), 'hongkong': School.query(School.country == "HongKong").fetch(), 'newzealand': School.query(School.country == "NewZealand").fetch(), 'southkorea': School.query(School.country == "SouthKorea").fetch(), 'sweden': School.query(School.country == "Sweden").fetch(), 'usa': School.query(School.country == "USA").fetch()}
            }
            template = jinja_environment.get_template('testcountries.html')
            self.response.out.write(template.render(template_values))
          else: #Not NUS account. Means no permission
            template_values = {
              'errormsg': 'gmail',
              'redirectlink': users.create_logout_url('/countries')
            }
            template = jinja_environment.get_template('loginerror.html')
            self.response.out.write(template.render(template_values))
        else:
            template_values = {
            'text': 'Login',
            'url':'/_ah/login_required?continue_url=/countries',
            'admin': users.is_current_user_admin(),
                'anocountries': ['australia', 'canada', 'china', 'germany', 'hongkong', 'newzealand', 'southkorea', 'sweden', 'usa'],
                'countries': {'china': "China", 'australia': "Australia", 'germany': "Germany", 'canada': "Canada",'hongkong': "Hong Kong", 'newzealand': 'New Zealand', 'southkorea': 'South Korea', 'sweden': 'Sweden', 'usa': 'United States of America'},
                'schools': {'australia':School.query(School.country == "Australia").fetch(), 'canada':School.query(School.country == "Canada").fetch(), 'china':School.query(School.country == "China").fetch(), 'germany':School.query(School.country == "Germany").fetch(), 'hongkong': School.query(School.country == "HongKong").fetch(), 'newzealand': School.query(School.country == "NewZealand").fetch(), 'southkorea': School.query(School.country == "SouthKorea").fetch(), 'sweden': School.query(School.country == "Sweden").fetch(), 'usa': School.query(School.country == "USA").fetch()}
            }

            template = jinja_environment.get_template('testcountries.html')
            self.response.out.write(template.render(template_values))

#class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
 # def get(self, resource):
  #  resource = str(urllib.unquote(resource))
   # blob_info = blobstore.BlobInfo.get(resource)
    #self.sed_blob(blob_info)

class AddUniversity(webapp2.RequestHandler):
    def get(self):
      if users.is_current_user_admin():
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url('/countries'),
          'upload_url': blobstore.create_upload_url('/addeduniversity')
        }
        template = jinja_environment.get_template('adduniversity.html')
        self.response.out.write(template.render(template_values))
      else: #Not NUS account. Means no permission
          template_values = {
            'errormsg': 'gmail',
            'redirectlink': users.create_logout_url(self.request.host_url)
          }
          template = jinja_environment.get_template('loginerror.html')
          self.response.out.write(template.render(template_values))

class AddedUniversity(blobstore_handlers.BlobstoreUploadHandler):
  def post(self):
    #self.response.write('<html><body>You wrote:<pre>')
    #self.response.write(cgi.escape(self.request.get('name')))
    #self.response.write('</pre></body></html>')

    upload_img = self.get_uploads('img')
    blob_info = upload_img[0]
    
    sch = School()
    sch.school_name=self.request.get('name')
    sch.school_name_short=self.request.get('short_name')
    sch.country=self.request.get('country')
    sch.state=self.request.get('state')
    sch.exchange_type=self.request.get('exchange_type')
    sch.academic_calendar=self.request.get('calendar')
    sch.recommended_fac=self.request.get_all('faculty')
    sch.mod_offered=self.request.get('modules')
    sch.picture=blob_info.key()
    sch.content=(self.request.get('abtschool'))  
    sch.overall_rating=0.0
    sch.cost_rating=0.0
    sch.life_rating=0.0
    sch.academics_rating=0.0
    sch.total_expenditure=0
    sch.accomcost=0
    sch.foodcost=0
    sch.transportcost=0
    sch.academic_needs=0
    sch.othercost=0
    sch.num_reviews=0 
    sch.mappings_count = 0 

    sch.content = quopri.decodestring(sch.content)
    sch.content = " ".join(sch.content.split()) #Remove all whitespaces
    logging.info("sch.content: %s" % sch.content)
    faculties = ""
    for fac in sch.recommended_fac:
      faculties = faculties + fac + " "
    
    index=search.Index(name="my_index3")
    
    my_document = search.Document(
      doc_id = sch.school_name_short,
      fields=[
        search.TextField(name='name', value=sch.school_name),
        search.TextField(name='short_name', value=sch.school_name_short),
        search.AtomField(name='country', value=sch.country),
        search.AtomField(name='state', value=sch.state),
        search.TextField(name='exchange_type', value=sch.exchange_type),
        search.TextField(name='calendar', value=sch.academic_calendar),
        search.TextField(name='faculty',value=faculties),
        search.TextField(name='about',value=sch.content),
        search.NumberField(name='overall_rating', value=0.0),
        search.NumberField(name='cost_rating',value=0.0),
        search.NumberField(name='life_rating',value=0.0),
        search.NumberField(name='academics_rating',value=0.0),
        search.NumberField(name='total_expenditure',value=0),
        search.NumberField(name='accomcost',value=0),
        search.NumberField(name='foodcost',value=0),
        search.NumberField(name='transportcost',value=0),
        search.NumberField(name='academic_needs',value=0),
        search.NumberField(name='othercost',value=0)])
    
    try:
      index.put(my_document)
    except search.PutError, e:
      logging.exception("Add failed")
    sch.put()
    self.redirect("/university?school=" + sch.school_name_short)

class ModuleMappings(webapp2.RequestHandler):
  def get(self):
    target = self.request.get('school')
    query = School.query(School.school_name_short.IN([target])).get()
     
    if users.is_current_user_admin():
      template_values = {
        'text': 'Logout',
        'url': users.create_logout_url('/modulemappings?school='+target),
        'school': query,
        'modules': query.mod_mappings,
        'admin': users.is_current_user_admin()
        }
      template = jinja_environment.get_template('modmappings.html')
      self.response.out.write(template.render(template_values))
    elif users.get_current_user():
      if users.get_current_user().email().find('nus') > 0: # NUS account. 
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url('/modulemappings?school='+target),
          'school': query,
          'modules': query.mod_mappings,
          'admin': users.is_current_user_admin()
        }
        template = jinja_environment.get_template('modmappings.html')
        self.response.out.write(template.render(template_values))
      else: #Not NUS account. Means no permission
          template_values = {
            'errormsg': 'gmail',
            'redirectlink': users.create_logout_url('/modulemappings?school='+target)
          }
          template = jinja_environment.get_template('loginerror.html')
          self.response.out.write(template.render(template_values))
    else:
      template_values = {
        'text': 'Login',
        'url':'/_ah/login_required?continue_url=/modulemappings?school='+target,
        'school': query,
        'modules': query.mod_mappings,
        'admin': users.is_current_user_admin()
        }

      template = jinja_environment.get_template('modmappings.html')
      self.response.out.write(template.render(template_values))

class Search(webapp2.RequestHandler):
  def get(self):
      if users.is_current_user_admin():
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url('/search'),
        }
        template = jinja_environment.get_template('search.html')
        self.response.out.write(template.render(template_values))

      elif users.get_current_user():
        if users.get_current_user().email().find('nus') > 0: # NUS account. 
          template_values = {
            'text': 'Logout',
            'url': users.create_logout_url('/search'),
          }
          template = jinja_environment.get_template('search.html')
          self.response.out.write(template.render(template_values))
        else: #Not NUS account. Means no permission
          template_values = {
            'errormsg': 'gmail',
            'redirectlink': users.create_logout_url('/search')
          }
          template = jinja_environment.get_template('loginerror.html')
          self.response.out.write(template.render(template_values))
      else:
        template_values = {
          'text': 'Login',
          'url':'/_ah/login_required?continue_url=/search'
        }
        template = jinja_environment.get_template('search.html')
        self.response.out.write(template.render(template_values))

class SearchResults(webapp2.RequestHandler):
  def get(self):
      if users.is_current_user_admin():
        text = 'Logout'
        url = users.create_logout_url('/search')
      elif users.get_current_user():
        if users.get_current_user().email().find('nus') > 0: # NUS account. 
          text = 'Logout'
          url = users.create_logout_url('/search')
        else: #Not NUS account. Means no permission
          template_values = {
            'errormsg': 'gmail',
            'redirectlink': users.create_logout_url('/search')
          }
          template = jinja_environment.get_template('loginerror.html')
          self.response.out.write(template.render(template_values))
      else:
        text ='Login'
        url = '/_ah/login_required?continue_url=/search'
      
      countries = self.request.get_all("country")
      expenditure = self.request.get_all("expenditure")
      course = self.request.get_all("course")
      keyword = self.request.get('keyword')


      def toSearch(lst):
        result = ""
        if lst:
          for (i, obj) in enumerate(lst):
            if i == len(lst) - 1:
              result = result + obj
            else:
              result = result + obj + " OR "
        return result
      def toSearchCost(lst):
        query = ""
        if lst:
          for (i, obj) in enumerate(lst):
            if i == len(lst) - 1:
              if obj == "one":
                query = query + "total_expenditure >= 0.0 AND total_expenditure <= 6000"
              elif obj == "two":
                query = query + "total_expenditure > 6000 AND total_expenditure <= 7000"
              elif obj == "three":
                query = query + "total_expenditure > 7000 AND total_expenditure <= 8000"
              elif obj == "four":
                query = query + "total_expenditure > 8000 AND total_expenditure <= 9000"
              elif obj == "five":
                query = query + "total_expenditure > 9000 AND total_expenditure <= 10000"
              elif obj == "six":
                query = query + "total_expenditure > 10000 AND total_expenditure <= 11000"
              elif obj == "seven":
                query = query + "total_expenditure > 11000"
            else:
              if obj == "one":
                query = query + "total_expenditure >= 0.0 AND total_expenditure <= 6000" + " OR "
              elif obj == "two":
                query = query + "total_expenditure > 6000 AND total_expenditure <= 7000" + " OR "
              elif obj == "three":
                query = query + "total_expenditure > 7000 AND total_expenditure <= 8000" + " OR "
              elif obj == "four":
                query = query + "total_expenditure > 8000 AND total_expenditure <= 9000" + " OR "
              elif obj == "five":
                query = query + "total_expenditure > 9000 AND total_expenditure <= 10000" + " OR "
              elif obj == "six":
                query = query + "total_expenditure > 10000 AND total_expenditure <= 11000" + " OR "
              elif obj == "seven":
                query = query + "total_expenditure > 11000" + " OR "

        return query

      if keyword:
        if keyword.lower() == "faculty of science":
          keyword = "FoS"
        elif keyword.lower() == "school of computing":
          keyword = "SoC"

      def res(query):
        if countries:
          query = 'country:' + toSearch(countries) 
          if course:
            query = query + " AND " + toSearch(course)
            if keyword:
              query = query + " AND " + keyword
              if expenditure:
                query = query + " AND " + toSearchCost(expenditure)
            else: 
              if expenditure:
                query = query + " AND " + toSearchCost(expenditure)
          else:
            if keyword:
              query = query + " AND " + keyword
              if expenditure: 
                query = query + " AND " + toSearchCost(expenditure)
            else:
              if expenditure:
                query = query + " AND " + toSearchCost(expenditure)
        else:
          if course:
            query = query + toSearch(course)
            if keyword:
              query = query + " AND " + keyword
              if expenditure:
                query = query + " AND " + toSearchCost(expenditure)
            else: 
              if expenditure:
                query = query + " AND " + toSearchCost(expenditure)
          else: 
            if keyword:
              query = query + keyword
              if expenditure:
                query = query + " AND " + toSearchCost(expenditure)
            else:
              if expenditure:
                query = query + toSearchCost(expenditure)
        return query

      schools = []
      query = ""
      try:
        index=search.Index(name='my_index3')
        results = index.search(res(query))
        for doc in results:
          schools.append(doc)
      except search.Error:
        logging.exception('Search failed')
      
      template_values = {
        'text': text,
        'url': url,
        'results': schools
      }

      template = jinja_environment.get_template('searchresults.html')
      self.response.out.write(template.render(template_values))




"""def check_name(request):
  name = request.POST['short_name']
  qry = School.query(school_name_short==name).get()
  if qry:
    msg = 'used'
  else:
    msg = 'available'

  if request.is_xhr:
    return {'msg':msg}
  else:
    request.response.content_type='text/html'
    return Response(json.dumps({'msg':msg}))"""
class CheckName(webapp2.RequestHandler):
  def post(self):
    name = self.request.get("short_name")
    qry = School.query(School.school_name_short==name).get()
    if qry:
      self.response.write("false")
    else:
      self.response.write("true")

class EditReview(webapp2.RequestHandler):
  def get(self):
    
    review_school = self.request.get('school')

    review_id = self.request.get('reviewid')
    review_key = ndb.Key(urlsafe=review_id)
    review = review_key.get()

    if users.is_current_user_admin():
      template_values = {
        'text': 'Logout',
        'url': users.create_logout_url('/countries'),
        'query': review_school,
        'reviewid': review_id,
        'review': review
      }
      template = jinja_environment.get_template('editreview.html')
      self.response.out.write(template.render(template_values))
    elif users.get_current_user():
      if users.get_current_user().email().find('nus') > 0: # NUS account. 
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url('/countries'),
          'query': review_school,
          'reviewid': review_id,
          'review': review
        }
        template = jinja_environment.get_template('editreview.html')
        self.response.out.write(template.render(template_values))
      else: #Not NUS account. Means no permission
          template_values = {
            'errormsg': 'gmail',
            'redirectlink': users.create_logout_url('/countries')
          }
          template = jinja_environment.get_template('loginerror.html')
          self.response.out.write(template.render(template_values))
    else:
      template_values = {
        'text': 'Login',
        'url':'/_ah/login_required?continue_url=/countries',
        'query': review_school,
        'reviewid': review_id,
        'review':review
      }
      template = jinja_environment.get_template('editreview.html')
      self.response.out.write(template.render(template_values))
  def post(self):
    
    review_school = self.request.get('school')
    query = School.query(School.school_name_short.IN([review_school])).get()
    num = query.num_reviews

    review_id = self.request.get('reviewid')
    review_key = ndb.Key(urlsafe=review_id)
    review = review_key.get()
    review.major = self.request.get('major')
    review.faculty = self.request.get('faculty') 
    review.year = self.request.get('year')
    review.semester = self.request.get('semester')

    overall = review.overall_rating
    review.overall_rating = int(self.request.get('overall'))
    query.overall_rating = (query.overall_rating * (num) - overall + review.overall_rating)/(num)
    cost = review.cost_rating
    review.cost_rating = int(self.request.get('cost'))
    query.cost_rating = ((query.cost_rating) * (num) - cost + review.cost_rating)/(num)
    life = review.life_rating
    review.life_rating = int(self.request.get('life'))
    query.life_rating = ((query.life_rating) * (num) - life + review.life_rating)/(num)
    academics = review.academics_rating
    review.academics_rating = int(self.request.get('academics'))
    query.academics_rating = ((query.academics_rating) * (num) - academics + review.academics_rating)/(num)

    accom = review.accommodation
    review.accommodation = int(self.request.get('accomcost'))
    query.accomcost = (query.accomcost * num - accom + review.accommodation)/(num)
    food = review.food 
    review.food = int(self.request.get('foodcost'))
    query.foodcost = (query.foodcost * num - food + review.food)/(num)
    transport = review.transport
    review.transport = int(self.request.get('transportcost'))
    query.transportcost = (query.transportcost * num - transport + review.transport)/(num)
    academic_needs = review.academic_needs
    review.academic_needs = int(self.request.get('acadcost'))
    query.academic_needs = (query.academic_needs * num - academic_needs + review.academic_needs)/(num)
    others = review.others
    review.others = int(self.request.get('othercost'))
    query.othercost = (query.othercost * num - others + review.others)/(num)
    review.total_expenditure = review.accommodation + review.food + review.transport + review.academic_needs + review.others
    query.total_expenditure = (query.total_expenditure * num - accom - food - transport - academic_needs - others + review.total_expenditure)/(num)
    review.content = self.request.get('reviewcontents')

    index=search.Index(name="my_index3")
    
    my_document = search.Document(
      doc_id = query.school_name_short,
      fields=[
        search.TextField(name='name', value=query.school_name),
        search.TextField(name='short_name', value=query.school_name_short),
        search.AtomField(name='country', value=query.country),
        search.AtomField(name='state', value=query.state),
        search.TextField(name='exchange_type', value=query.exchange_type),
        search.TextField(name='calendar', value=query.academic_calendar),
        search.TextField(name='faculty',value=review.faculty),
        search.TextField(name='about',value=query.content),
        search.NumberField(name='overall_rating', value=query.overall_rating),
        search.NumberField(name='cost_rating',value=query.cost_rating),
        search.NumberField(name='life_rating',value=query.life_rating),
        search.NumberField(name='academics_rating',value=query.academics_rating),
        search.NumberField(name='total_expenditure',value=query.total_expenditure),
        search.NumberField(name='accomcost',value=query.accomcost),
        search.NumberField(name='foodcost',value=query.foodcost),
        search.NumberField(name='transportcost',value=query.transportcost),
        search.NumberField(name='academic_needs',value=query.academic_needs),
        search.NumberField(name='othercost',value=query.othercost)])
    
    try:
      index.put(my_document)
    except search.PutError, e:
      logging.exception("Add failed")

    count = query.mappings_count

    if self.request.get('mod1') != '':
      mod1 = Mapping()
      mod1.sep_mod = self.request.get('mod1')
      mod1.sep_mc = int(self.request.get('cred1'))
      mod1.nus_mod = self.request.get('nmod1')
      mod1.nus_mc = int(self.request.get('mc1'))
      mod1.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod1)

    if self.request.get('mod2') != '':
      mod2 = Mapping()
      mod2.sep_mod = self.request.get('mod2')
      mod2.sep_mc = int(self.request.get('cred2'))
      mod2.nus_mod = self.request.get('nmod2')
      mod2.nus_mc = int(self.request.get('mc2'))
      mod2.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod2)

    if self.request.get('mod3') != '':
      mod3 = Mapping()
      mod3.sep_mod = self.request.get('mod3')
      mod3.sep_mc = int(self.request.get('cred3'))
      mod3.nus_mod = self.request.get('nmod3')
      mod3.nus_mc = int(self.request.get('mc3'))
      mod3.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod3)

    if self.request.get('mod4') != '':
      mod4 = Mapping()
      mod4.sep_mod = self.request.get('mod4')
      mod4.sep_mc = int(self.request.get('cred4'))
      mod4.nus_mod = self.request.get('nmod4')
      mod4.nus_mc = int(self.request.get('mc4'))
      mod4.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod4)

    if self.request.get('mod5') != '':
      mod5 = Mapping()
      mod5.sep_mod = self.request.get('mod5')
      mod5.sep_mc = int(self.request.get('cred5'))
      mod5.nus_mod = self.request.get('nmod5')
      mod5.nus_mc = int(self.request.get('mc5'))
      mod5.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod5)

    if self.request.get('mod6') != '':
      mod6 = Mapping()
      mod6.sep_mod = self.request.get('mod6')
      mod6.sep_mc = int(self.request.get('cred6'))
      mod6.nus_mod = self.request.get('nmod6')
      mod6.nus_mc = int(self.request.get('mc6'))
      mod6.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod6)

    if self.request.get('mod7') != '':
      mod7 = Mapping()
      mod7.sep_mod = self.request.get('mod7')
      mod7.sep_mc = int(self.request.get('cred7'))
      mod7.nus_mod = self.request.get('nmod7')
      mod7.nus_mc = int(self.request.get('mc7'))
      mod7.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod7)

    if self.request.get('mod8') != '':
      mod8 = Mapping()
      mod8.sep_mod = self.request.get('mod8')
      mod8.sep_mc = int(self.request.get('cred8'))
      mod8.nus_mod = self.request.get('nmod8')
      mod8.nus_mc = int(self.request.get('mc8'))
      mod8.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod8)

    if self.request.get('mod9') != '':
      mod9 = Mapping()
      mod9.sep_mod = self.request.get('mod9')
      mod9.sep_mc = int(self.request.get('cred9'))
      mod9.nus_mod = self.request.get('nmod9')
      mod9.nus_mc = int(self.request.get('mc9'))
      mod9.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod9)

    if self.request.get('mod10') != '':
      mod10 = Mapping()
      mod10.sep_mod = self.request.get('mod10')
      mod10.sep_mc = int(self.request.get('cred10'))
      mod10.nus_mod = self.request.get('nmod10')
      mod10.nus_mc = int(self.request.get('mc10'))
      mod10.map_id = count
      count = count + 1
      (query.mod_mappings).append(mod10)

    query.mappings_count = count

    query.put()
    review.put()

    self.redirect("/university?school=" + review_school)

class EditUni(webapp2.RequestHandler):
  def get(self):
      target = self.request.get('school')
      query = School.query(School.school_name_short.IN([target])).get()
      if users.is_current_user_admin():
        template_values = {
          'text': 'Logout',
          'url': users.create_logout_url('/university?school=' + target),
          'school': query
        }
        template = jinja_environment.get_template('edituni.html')
        self.response.out.write(template.render(template_values))
      else: 
          template_values = {
            'errormsg': 'gmail',
            'redirectlink': users.create_logout_url('/university?school=' + target)
          }
          template = jinja_environment.get_template('loginerror.html')
          self.response.out.write(template.render(template_values))
  def post(self):
      target = self.request.get('school')
      query = School.query(School.school_name_short.IN([target])).get()

      query.school_name=self.request.get('name')
      query.country=self.request.get('country')
      query.state=self.request.get('state')
      query.exchange_type=self.request.get('exchange_type')
      query.academic_calendar=self.request.get('calendar')
      query.recommended_fac=self.request.get_all('faculty')
      query.mod_offered=self.request.get('modules')
      query.content=(self.request.get('abtschool'))  
      query.put()

      index=search.Index(name="my_index3")
      faculties = ""
      for fac in query.recommended_fac:
        faculties = faculties + fac + " "
    
      my_document = search.Document(
        doc_id = query.school_name_short,
        fields=[
        search.TextField(name='name', value=query.school_name),
        search.TextField(name='short_name', value=query.school_name_short),
        search.AtomField(name='country', value=query.country),
        search.AtomField(name='state', value=query.state),
        search.TextField(name='exchange_type', value=query.exchange_type),
        search.TextField(name='calendar', value=query.academic_calendar),
        search.TextField(name='faculty',value=faculties),
        search.TextField(name='about',value=query.content),
        search.NumberField(name='overall_rating', value=query.overall_rating),
        search.NumberField(name='cost_rating',value=query.cost_rating),
        search.NumberField(name='life_rating',value=query.life_rating),
        search.NumberField(name='academics_rating',value=query.academics_rating),
        search.NumberField(name='total_expenditure',value=query.total_expenditure),
        search.NumberField(name='accomcost',value=query.accomcost),
        search.NumberField(name='foodcost',value=query.foodcost),
        search.NumberField(name='transportcost',value=query.transportcost),
        search.NumberField(name='academic_needs',value=query.academic_needs),
        search.NumberField(name='othercost',value=query.othercost)])
      
      try:
        index.put(my_document)
      except search.PutError, e:
        logging.exception("Add failed")

      self.redirect('/university?school=' + target)
    
class DeleteUni(webapp2.RequestHandler):

  def get(self):
    
    school = self.request.get('school')
    query = School.query(School.school_name_short.IN([school])).get()
    ancestor_key = ndb.Key("School", school or "*notitle*")
    comments = Comments.query_book(ancestor_key).fetch()
    ancestor_key_review = ndb.Key("School", school or "*notitle*")
    reviews = Review.query_review(ancestor_key_review).fetch()

    uniid = self.request.get('uniid')
    unikey = ndb.Key(urlsafe=uniid)
    unikey.delete()

    for comment in comments:
      comment_id = comment.key.urlsafe()
      comment_key = ndb.Key(urlsafe=comment_id)
      comment_key.delete()
    for review in reviews:
      review_id = review.key.urlsafe()
      review_key = ndb.Key(urlsafe=review_id)
      review_key.delete()
    doc_id = school

    index=search.Index(name='my_index3')
    try:
      index.delete(doc_id)
    except search.Error:
      logging.exception("Error removing doc id %s.", doc_id)
    self.redirect("/countries")
    
class DeleteMapping(webapp2.RequestHandler):
  def get(self):
    target = self.request.get('school')
    school = School.query(School.school_name_short.IN([target])).get()
    mapping_id = int(self.request.get('id'))
    school.mod_mappings = filter(lambda mapping: mapping.map_id != mapping_id, school.mod_mappings)
    school.put()
    self.redirect('/modulemappings?school='+target)

app = webapp2.WSGIApplication([('/', MainPage),
                                ('/login', Login),
                                ('/about', About),
                                ('/contact', Contact),
                                ('/countries', Countries),
                                ('/university', University),
                                ('/tosubmitreview', ToSubmitReview),
                                ('/submittedreview', SubmittedReview),
                                ('/deletereview', DeleteReview),
                                ('/deletecomment', DeleteComment),
                                ('/adduniversity', AddUniversity),
                                ('/addeduniversity', AddedUniversity),
                                ('/search', Search),
                                ('/modulemappings', ModuleMappings),
                                ('/check_name', CheckName),
                                ('/editreview', EditReview),
                                ('/edituni', EditUni),
                                ('/deleteuni', DeleteUni),
                                ('/deletemapping', DeleteMapping),
                                ('/searchresults', SearchResults)],
                              debug=True)
