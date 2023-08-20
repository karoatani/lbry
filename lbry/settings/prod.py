import os
import dj_database_url
from .common import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://*.lbry-production.up.railway.app/','https://lbry-production.up.railway.app/*']

DATABASES = {
    'default': dj_database_url.config(),
}
