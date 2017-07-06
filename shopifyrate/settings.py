"""
Django settings for shopifyrate project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# React application directory
REACT_APP_DIR = os.path.join(BASE_DIR, 'frontend')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w6i-pl(5(wvliuq#*$hj_*ct5pg%q51j12s=^3!c44dg32)pr0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shopify_auth',
    'shopifyrate_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'shopifyrate.urls'

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
                'shopify_auth.context_processors.shopify_auth',
            ],
        },
    },
]

WSGI_APPLICATION = 'shopifyrate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbfdje73kidbju',
        'USER': 'qarbaxvmufdgpz',
        'PASSWORD': 'e9713e53e64b60fc7434fccd2a2d26110d2e35229ede5e3bcf87a0512a5a3e34',
        'HOST': 'ec2-23-21-246-11.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(REACT_APP_DIR, 'build', 'static'),
    os.path.join(REACT_APP_DIR, 'build'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Facebook credentials
FACEBOOK_APP_ID = '269457056812449'
FACEBOOK_APP_SECRET = 'bcaf9d9d002325a7cb219e98d61da10c'
FACEBOOK_MAIN_AD_ACCOUNT = 'act_114787645721020'
FACEBOOK_TEST_TOKEN = 'EAAD1EdwnTaEBAAiPpQqiVWZByw7pkAKmAue9om28mygOZAw11TacPK4qZCQWZBNZC0Bb459daUXcFmTtzdoiZCJ0wvd2SWO' \
                      'IFN2ZBZCR01wWBTSrnh1NarO4ZBr1jruHCZA2qCFZAZBQ9x7CcbZCt5azMfP2BjQv3nRZATOU2LKCFtXO5gIQBXsvEM0ZAaSiZAs67XMEhY0ZD'

# Shopify integration
SHOPIFY_APP_IS_EMBEDDED = True
SHOPIFY_APP_DEV_MODE = False
SHOPIFY_APP_NAME = 'Rate'
SHOPIFY_APP_API_KEY = '26fa87e06de227bd244565aab90fd781'
SHOPIFY_APP_API_SECRET = '4f172633d87fa04348941782772e8764'
SHOPIFY_APP_API_SCOPE = ['read_products', 'write_products', 'read_orders']
# Use the Shopify Auth authentication backend as the sole authentication backend.
AUTHENTICATION_BACKENDS = ['shopifyrate_app.backends.ShopUserBackend']
# Set the login redirect URL to the "home" page for your app (where to go after logging on).
LOGIN_REDIRECT_URL = 'https://shopifyrate.herokuapp.com/'
LOGIN_URL = 'https://shopifyrate.herokuapp.com/login/'
# Set secure proxy header to allow proper detection of secure URLs behind a proxy.
# This ensures that correct 'https' URLs are generated when our Django app is running behind a proxy like nginx, or is
# being tunneled (by ngrok, for example).
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Use the Shopify Auth user model.
AUTH_USER_MODEL = 'shopifyrate_app.AuthAppShopUser'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
