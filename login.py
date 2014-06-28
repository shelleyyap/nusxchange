import urllib
import webapp2

from google.appengine.api import users

class LoginHandler(webapp2.RequestHandler):
  def get(self):
  	url = self.request.get('continue_url')
  	if url=="" or url == None:
	    self.redirect(users.create_login_url('/', None, federated_identity='https://openid.nus.edu.sg/'))
	else:
		self.redirect(users.create_login_url(url, None, federated_identity='https://openid.nus.edu.sg/'))

app = webapp2.WSGIApplication([('/_ah/login_required', LoginHandler)],
                              debug=True)
