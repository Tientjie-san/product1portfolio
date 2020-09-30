"""
Django settings for product1_portfolio project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '21&u-v0iff^0%n0o@sml_vv$zt7!81hl8j#l61-ol5(b60=!*q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://sebastiaanportfolio.herokuapp.com/', 'localhost']


# Application definition

INSTALLED_APPS = [
    'portfolio.apps.PortfolioConfig',
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'product1_portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'portfolio.context_processors.add_variable_to_context'
            ],
        },
    },
]

WSGI_APPLICATION = 'product1_portfolio.wsgi.application'
AUTH_USER_MODEL = 'account.User'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

## database voor local.
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES['default'].update(db_from_env)


# DATABASE voor heroku
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd2j06hav93fu4m',
        'HOST': 'ec2-54-75-199-252.eu-west-1.compute.amazonaws.com',
        'PORT': 5432,
        'USER': 'ssnrheradadtez' ,
        'PASSWORD': 'f7dfa81d5bde21a157f5feb43edc0d9692781d134d9b4d969f50ffc9f1a26b5d'

    }
}
# postgres://ssnrheradadtez:f7dfa81d5bde21a157f5feb43edc0d9692781d134d9b4d969f50ffc9f1a26b5d@ec2-54-75-199-252.eu-west-1.compute.amazonaws.com:5432/d2j06hav93fu4m

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = BASE_DIR/'staticfiles'
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR/'media'
MEDIA_URL = '/media/'


# STATICFILES_DIRS = (BASE_DIR/'static',)


# Activate Django-Heroku.
django_heroku.settings(locals())