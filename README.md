[![PyPI release](https://badge.fury.io/py/iitb-oauth.svg)](https://badge.fury.io/py/iitb-oauth)
![Travis-ci](https://api.travis-ci.org/nautatva/iitb_oauth.svg)
[![Python versions](https://img.shields.io/pypi/pyversions/iitb-oauth.svg)](https://pypi.org/project/iitb-oauth/)
[![License](https://img.shields.io/pypi/l/iitb-oauth.svg)](https://pypi.org/project/iitb-oauth/)


# Django Oauth2 Client to authenticate using IIT Bombay gymkhana SSO
A small package for LDAP authentication using IIT Bombay gymkhana SSO.


## Motivation
SSO can be a tricky thing to setup and bugs can be time consuming to debug. With people moving away from PHP to Django and node, this module can be used to quickly define custom callbacks that map the user details obtained from IIT Bombay gymkhana SSO to your Django user model. You get a quick and easy way to programatically create users once they are authenticated.


## Setting up in your app
For using this Django app, the following steps must be done:

```python
INSTALLED_APPS = [
   # ...
    'iitb_oauth'
   # ...
]
```

```python
AUTHENTICATION_BACKENDS = [
# ...
'iitb_oauth.backend.OauthBackend'
# ...
]
```

Step 2:  Add the oauth urls to the root website:
```python
urlpatterns = [
    # ...
    url(r'', include('iitb_oauth.urls')),
    # ...
]
```


Step 3: Add the LOGIN_URL and corresponding OAUTH config settings for your application. 
Also add the `FALLBACK_URL` as a fallback in case OAuth authentication fails. Example:

```python
LOGIN_URL = "/login/"
FALLBACK_URL = "/" # In case user is not logged in or doesn't have enough permissions to view the content


CLIENT_ID = 'my-id'
CLIENT_SECRET = '<secret>'

SCOPE = 'ldap'  # ldap is necessary for login, pass only necessary scopes. seperate with spaces
# Eg: SCOPE = 'profile ldap program'

FIELDS = 'username' # username is mandatory field. seperate with commas
# Eg: FIELDS = 'username,first_name,last_name,email,roll_number'

REDIRECT_URI = '<app_redirect_url>' # should end with /oauth/complete (the view is provided by this app)

LOGIN_COMPLETE_REDIRECT = '/some/url/in/your/app'
LOGOUT_REDIRECT = '/' # redirect to this URL after logout.
MAPPINGS = {
    # fields in User model: "LDAP attributes"
    # email mapped with username@iitb.ac.in if email is not in scope.
    "first_name": "first_name",
    "last_name": "last_name"
}  # In case a custom User model is defined, map fields in User model: "LDAP attributes"
```


## Usage
Once you try to access some endpoint that has the `@login_required` decorator on top of it, you'll be redirected to the login URI that you defined. The user is authenticated using IITB gymkhana SSO and any other backends you provided. Upon successful authentication the url specified in `LOGIN_COMPLETE_REDIRECT` are called and the callbacks are used to shape your user into the form that you've provided. If authentication fails due to any reason or if the user does not have permission, he will be redirected to the URI specified in `FALLBACK_URL`.


## License
MIT
