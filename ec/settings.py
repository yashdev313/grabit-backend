"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vzi^v!ch9tr^k)r$(*h#az)9@n68#ij96i+yu4!eid8#colz&c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']

STRIPE_SECRET_KEY ='sk_test_51Nb5YRSIszTuRq5HT3QVf9CXqQQCcGEJ5DVUQV6K6ZBGiGCVKOTPdlozh2DHP0CXkxgzGoeFYMuI1mwVx8P6HYpi00fKMU83yC'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    #'rest_framework_simplejwt',
    'authentication',
    'corsheaders',
    'api',
    'payment',
    'ckeditor',
    'rest_framework.authtoken',
    'django_filters',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ec.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'ec.wsgi.app'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# additional fields
AUTH_USER_MODEL ="authentication.CustomUser"

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '2c4c3c6c5dbfdb'
EMAIL_HOST_PASSWORD = 'd2e9c14b39ffcd'
EMAIL_PORT = '2525'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
      #'rest_framework_simplejwt.authentication.JWTAuthentication',
'rest_framework.authentication.SessionAuthentication',
    )
}

# core/settings.py

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    "SIGNING_KEY": "complexsigningkey",  # generate a key and replace me
    "ALGORITHM": "HS512",
}

CORS_ALLOWED_ORIGINS = [
        "https://localhost:3000",
        "https://127.0.0.1:3000",
    ]

CSRF_TRUSTED_ORIGINS = [
    "https://localhost:3000",  # Example: if your Next.js runs on localhost:3000
    "https://127.0.0.1:3000"
]

CORS_ALLOW_CREDENTIALS = True


# CORS_ALLOW_HEADERS = "*"
CORS_ALLOW_HEADERS = 'access-control-allow-origin'
CORS_ALLOW_HEADERS = [
    'Content-Type',
    'Authorization',
    'x-csrftoken',
    'access-control-allow-origin'
    'common',
    # Add other headers you want to allow.
]


# if DEBUG:
#     CORS_ALLOW_ALL_ORIGINS = True
# else:
#     CORS_ALLOWED_ORIGINS = [
#         "http://localhost:3000/",
#         "http://127.0.0.1:3000/",
#     ]

CSRF_COOKIE_SAMESITE ="None"
SESSION_COOKIE_SAMESITE ="None"
CSRF_COOKIE_SECURE= False
SESSION_COOKIE_SECURE = True



STATIC_URL = "static/"
STATIC_ROOT  = BASE_DIR / 'static'
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

# TEMPLATES_ROOT = BASE_DIR/'api/templates'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# CKEDITOR_BASEPATH = "/my_static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH='uploads/'

# CSRF_USE_SESSIONS=True
# HTTP_X_CSRFTOKEN = "CSRFToken"

# this is default name django expects to be sent along in request
# "X-CSRFToken": csrfCookie?.value,

# CSRF_COOKIE_NAME ="XCSRF_TOEJN"
CSRF_COOKIE_HTTPONLY = False
# CSRF_COOKIE_DOMAIN 
# CSRF_HEADER_NAME ="CSRFToken"



# STRIPE_SECRET_KEY ='sk_test_51Nb5YRSIszTuRq5HT3QVf9CXqQQCcGEJ5DVUQV6K6ZBGiGCVKOTPdlozh2DHP0CXkxgzGoeFYMuI1mwVx8P6HYpi00fKMU83yC'


# SITE_URL='http://localhost:3000/'



# # STRIPE_PUBLIC_KEY="pk_test_51IBev4JnWlmnG27uqt62oM3NULHTQYULGaA2BroTxffTYvErhxSqZrerC2mjl8wKEJ8TeqLoEykUiV8A4ibSOOZs00DQBfokyW"

# STRIPE_SECRET_WEBHOOK=" whsec_ece5fd8f4265034dac84f5924c178bf7af7a86072c268194f0775363bb1d5aef"
# # STRIPE_SECRET_WEBHOOK="whsec_mwXBR7ZwLZe5XTFPlDekNrQeFaqrXkNj"

#  # whsec_ece5fd8f4265034dac84f5924c178bf7af7a86072c268194f0775363bb1d5aef

