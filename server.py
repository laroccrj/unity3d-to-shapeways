from shapeways.client import Client
import keys
import base64

__author__ = 'rob'

client = Client(consumer_key=keys.__consumer_key__,
                consumer_secret=keys.__consumer_secret__,
                oauth_token=keys.__oauth_token__,
                oauth_secret=keys.__oauth_secret__)
model_file = open("cube.stl", "rb")
file_contents = base64.b64encode(model_file.read())
params = {
    "file": file_contents,
    "fileName": "cube.stl",
    "hasRightsToModel": True,
    "acceptTermsAndConditions": True,
}
print client.add_model(params)