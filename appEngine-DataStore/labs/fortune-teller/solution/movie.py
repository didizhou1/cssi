
from google.appengine.ext import ndb


class Movie(ndb.Model):
    title = ndb.StringProperty(required=True)
    media_type = ndb.StringProperty(required=True, default = 'Movie')
    runtime = ndb.FloatProperty(required=False)
    rating = ndb.FloatProperty(required=False)

    
    # def __init__(self, mov_title, type, runtime, user_rating):
    #     self.title = mov_title
    #     self.media_type = type
    #     self.runtime = runtime
    #     self.rating = user_rating

class TVShow(ndb.Model):
    title = ndb.StringProperty(required=True)
    media_type = ndb.StringProperty(required=True, default = 'TV')
    runtime = ndb.StringProperty(required=False)
    rating = ndb.FloatProperty(required=False)

class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    username = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=False)
    billing_address = ndb.StringProperty(required=False)

    # def __init__(self, name, user, passw, email, billing):
    #     self.name = name
    #     self.username = user
    #     self.password = passw
    #     self.email = email
    #     self.billing_address = billing
