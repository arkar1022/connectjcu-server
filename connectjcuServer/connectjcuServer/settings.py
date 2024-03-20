"""
Django settings for connectjcuServer project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get("DEBUG", "FALSE").lower() == "true"
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['0.0.0.0','localhost','45.32.108.232','https://connectjcu-client.vercel.app']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    'rest_framework_simplejwt.token_blacklist',
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "accounts",
    "api",
    "corsheaders",
]

MIDDLEWARE = [ 
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "connectjcuServer.urls"
# CORS_URLS_REGEX = r"^/api/.*" 
CORS_ALLOWED_ORIGINS = [
    'https://connectjcu-client.vercel.app',
    'http://localhost:3000',
    'https://localhost:3000',
]

CSRF_TRUSTED_ORIGINS = [
    'https://connectjcu-client.vercel.app',
    'http://localhost:3000',
    'https://localhost:3000',
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "connectjcuServer.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

AUTH_USER_MODEL= "accounts.User"

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'connectjcuServer','static')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR,'connectjcuServer', "static"),
# ]

MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'connectjcuServer','media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'connectjcuteam@gmail.com'
EMAIL_HOST_PASSWORD = 'dvlawxcwxclejhrj'
EMAIL_PORT = 587
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL='connectjcuteam@gmail.com'
EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'
 
# EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# DEFAULT_FROM_EMAIL = 'info@connectjcu.com'
# EMAIL_PORT = '2525'
# EMAIL_USE_TLS=True
