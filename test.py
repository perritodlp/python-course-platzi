# import google
# print("google path: {} ".format(google.__path__))

""" import google
import sys

gae_dir = google.__path__.append('/Users/ferengifo/Sites/curso-inteligencia-artificial/curso-python/google-cloud-sdk/platform/google_appengine/google')
sys.path.insert(0, gae_dir) # might not be necessary
import google.appengine # now it's on your import path` """

from google.cloud import ndb
client = ndb.Client()
print(client)