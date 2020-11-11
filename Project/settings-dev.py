'''
   @ Author     Kuntal
   @ version    0.1
   @date        29/04/2020
'''
from .settings import *
import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY', default="unsafe-secret-key")
DEBUG = env('DEBUG', default=True)

ALLOWED_HOSTS = ALLOWED_HOSTS + [
    '*',
]

INSTALLED_APPS = INSTALLED_APPS + [
    'App',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
]

# Sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


####################################
    ##  CKEDITOR CONFIGURATION ##
####################################
 
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
 
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
 
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}
 
###################################


# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "a@b.com"
EMAIL_HOST_PASSWORD = ""

