from pathlib import Path
import os, environ, django_heroku, dj_database_url
from urllib.parse import urlparse
from decouple import config

env = environ.Env()
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['https://www.bestoff.cl', 'www.bestoff.cl', 'bestoff.cl','https://bestoff.cl', 'http://127.0.0.1', '127.0.0.1', 'https://bestoff-cl.herokuapp.com', 'bestoff-cl.herokuapp.com']

CSRF_TRUSTED_ORIGINS = ['https://www.bestoff.cl','https://bestoff.cl','http://127.0.0.1', 'https://bestoff-cl.herokuapp.com' ]

INSTALLED_APPS = [
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.sitemaps',

    'core',
    'propiedades',
    'acceso',

    'tailwind',
    'theme',

    'storages',
]


WSGI_APPLICATION = 'bestoff.wsgi.application'
ASGI_APPLICATION = 'bestoff.asgi.application'

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [ '127.0.0.1']
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    #'channels.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF =env('ROOT_URLCONF')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.csrf',
            ],
        },
    },
]




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddm83mt61ae18g',
        'USER': 'edohviiyeubwsl',
        'PASSWORD': 'ad07ac68b47248534b766eb57cc6cffd0fbab9b0456e428c99d8ae05300652ad',
        'HOST': 'ec2-52-204-195-41.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
'''
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

'''
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# Security
SECURE_CROSS_ORIGIN_OPENER_POLICY = None

#S3 BUCKETS CONFIG
AWS_ACCESS_KEY_ID = 'AKIA6D5N4TJSFEUQ4LG7'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'bestoff-cl'

AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'