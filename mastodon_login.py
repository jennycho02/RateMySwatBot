from mastodon import Mastodon
import requests
f = open("./user_token",'r')
token = f.readlines()[0]

m = Mastodon(access_token=token, api_base_url="https://social.cs.swarthmore.edu")

m.toot("Test post via API using OAuth")

