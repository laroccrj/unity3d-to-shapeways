from shapeways.client import Client
import keys
from urlparse import parse_qs
__author__ = 'rob'

client = Client(keys.__consumer_key__, keys.__consumer_secret__)
url = client.connect()
data = parse_qs(url.split('?')[1])
token = data.get("oauth_token", [None])[0]
print url
verifierCode = raw_input("Verifier Code: ")
url = url + "&oauth_verifier=" + verifierCode
client.verify_url(url)
print 'Token: ' + client.oauth_token
print 'Secret: ' + client.oauth_secret
