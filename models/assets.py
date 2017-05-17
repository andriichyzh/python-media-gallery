from google.appengine.ext import ndb


class Assets(ndb.Expando):
    name = ndb.StringProperty(required=True, default='Empty Name')
    description = ndb.TextProperty(required=True, default='Empty Description')
    original = ndb.StringProperty(required=False)
    url = ndb.StringProperty(required=True)
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
