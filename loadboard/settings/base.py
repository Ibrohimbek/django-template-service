import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'n#6f8%xk*hdw-syh(efjrw0%_6jqj5dpyuakxh*!nso4*-p%kl'

DEBUG = False

ADMINS = [
    ('Ibrohim Ermatov', 'ibrohim@mysuperdispatch.com'),
]

ALLOWED_HOSTS = [
    '*.superdispatch.org',
    '*.mysuperdispatch.com',
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',

    'loadboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'loadboard.api.urls'

WSGI_APPLICATION = 'loadboard.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'ORDERING_PARAM': 'ordering',
}
