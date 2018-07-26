"""
Django settings for dedupper_app project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import django_heroku
import dj_database_url
from django.conf.locale.en import formats as en_formats
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ulm$oueq%7j8ao9(@7j_y_rc-(!0b!!u***q2(5bx(-$!!teyx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#yo mama
# Application definition
# yo daddy


INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'dedupper.apps.DedupperConfig',
    'django.contrib.postgres',
    'django_tables2',
    'django_filters',
    'import_export',
    # 'celery_progress',
   # 'heroku_connect',
   # 'connect_client',

]

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dedupper_app.urls'
IMPORT_EXPORT_USE_TRANSACTIONS = True


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')] ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]

WSGI_APPLICATION = 'dedupper_app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'falcon_dup',
        'USER': 'jachi',
        'PASSWORD': '7924',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

'''
HEROKU_CONNECT_DATABASE_URL = os.environ['HEROKU_CONNECT_DATABASE_URL']
HEROKU_CONNECT_SCHEMA = os.environ['HEROKU_CONNECT_SCHEMA']
DATABASES = {
    'default': dj_database_url.config(default=HEROKU_CONNECT_DATABASE_URL),
}

DATABASES['default'] = dj_database_url.config(
    engine='heroku_connect.db.backends.postgresql'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dafi1ss9nanhc2',
        'USER': 'xkdyqhyazyiycb',
        'PASSWORD': 'eaa746a26096a351fc3e480236d417309679113b0d790953c077ec8540ac2a98',
        'HOST': 'ec2-23-23-247-245.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
'''
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
en_formats.DATETIME_FORMAT = "%d-%m-%Y_%H:%M:%S"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "/staticfiles")

'''
if local host can't connect, set configs via -> heroku config:set DJANGO_SETTINGS_MODULE=settings.heroku
'''
django_heroku.settings(locals())

REP_CSV = os.path.join(BASE_DIR, 'uploads', 'rep_csv.pkl')
SF_CSV = os.path.join(BASE_DIR, 'uploads', 'SF_csv.pkl')