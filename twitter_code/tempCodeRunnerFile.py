API_KEY = 'LzT8VLb7Xa6dwUjpvdovBsCrK'
API_SECRET = 'rBUe0vmhkmE7QD9cEv6L4DVvFHLvIzZU9alVqYQMdGTmbNgwZd'
ACCESS_KEY = '1586352690434641922-eJ05RDWMk4kwll7XUjl2DUMbvNj35V'
ACCESS_SECRET = 'AKAyiOiCfZQAKdnAF1Dh27KeMy43M8YgipnJAMJW3i81I'
import json
import tweepy
import requests
import config



auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status("On June 29th vs the Chicago White Sox, after being activated from the paternity list, Seth Brown had a wRC+ of 619. 519 percent better than the MLB league average. #Oakland #Athletics")
