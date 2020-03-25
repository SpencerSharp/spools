# # Steps:
# # Set up a local webserver at localhost and a port to take the redirects
# # User enters "spools login XXX"
# # Will auto open the link in their browser, and say "Opening <url>" in their terminal
# # User enters their login information into the browser
# # They are redirected to the webserver, where the information that we need is in the URL
# # We save the information into the .spools directory, encrypting information that we're able to

# import requests, os, json
# from requests_oauthlib import OAuth2Session
# from flask import Flask, request, redirect, session, url_for

# #username = 'SpencerSharp'

# #base_url = 'https://api.github.com'.format(username=username)
# app_auth_url = 'https://github.com/login/oauth/authorize'

# # Steps:
# # Set up a local webserver at localhost and a port to take the redirects
# # User enters "spools login XXX"
# # Will auto open the link in their browser, and say "Opening <url>" in their terminal
# # User enters their login information into the browser
# # They are redirected to the webserver, where the information that we need is in the URL
# # We save the information into the .spools directory, encrypting information that we're able to

# # def post(path,auth=(username,''),params=None):
# # 	return requests.post(base_url+path,auth=auth,data=json.dumps(params))

# # def get(path,auth=(username,''),params=None):
# # 	return requests.get(base_url+path,auth=auth)

# def basic_auth():
# 	return get('/')

# def create_auth():
# 	scopes = ['repo']
# 	note = 'Creating Spools Profile'
# 	params = {'scopes':scopes, 'note':note}
# 	return post('/authorizations',params=params)

# def create_repo():
# 	name = 'spools-profile'
# 	private = True
# 	return post('/user/repos')

# # curl -iv -u SpencerSharp -d '{"scopes":["public_repo"]}' https://api.github.com/authorizations

# os.environ['DEBUG'] = "1"
# client_id = '0c8dc5fac9c5f4a83881'
# github = OAuth2Session(client_id)
# authorization_url, state = github.authorization_url(auth_base_url)
# print(authorization_url)
# print(redirect(authorization_url))
# #print(res.__dict__.keys())
# #auth = os.system('curl -u "{username}" https://api.github.com'.format(username=username))






# # print(r)

# # URL = "https://api.github.com/users/{username}/repos".format(username=username)

# # r = requests.post(url = URL)
  
# # # extracting data in json format 
# # data = r.json()

# # print(data)