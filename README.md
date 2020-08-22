# qmon

A simple server monitoring solution using Django, Django Rest Framework, and psutil.

## Deploy to heroku

```
heroku create --buildpack https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python

heroku config:set SECRET_KEY=xxx
heroku config:set ALLOWED_HOSTS=.herokuapp.com
heroku config:set DEBUG=False
heroku config:set DISABLE_COLLECTSTATIC=1
```
