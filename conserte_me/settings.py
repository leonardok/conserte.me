import os
import sys
import django
import logging


SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
BASE_ROOT = os.path.abspath(os.path.join(SITE_ROOT, os.pardir))
# Django settings for conserte_me project.

DEBUG = os.environ['DEBUG']
TEMPLATE_DEBUG = DEBUG

RUNNING_DEVSERVER = (sys.argv[1] == 'runserver')

ADMINS = (
    ('Leonardo Korndorfer', 'leokorndorfer@gmail.com'),
)

MANAGERS = ['leokorndorfer@gmail.com', 'cristianobfernandes@gmail.com']


DATABASES = {
    'default': {
        'ENGINE': os.environ['DATABASE_ENGINE'], # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.environ['DATABASE_NAME'],     # Or path to database file if using sqlite3.
        'USER': os.environ['DATABASE_USER'],     # Not used with sqlite3.
        'PASSWORD': os.environ['DATABASE_PASSWORD'],  # Not used with sqlite3.
        'HOST': os.environ['DATABASE_HOST'],     # Set to empty string for localhost. Not used with sqlite3.
        'PORT': os.environ['DATABASE_PORT'],     # Set to empty string for default. Not used with sqlite3.
    }
}


# email settings
# These are the smtp settings for gmail
EMAIL_HOST          = 'mail.conserte.me'
EMAIL_HOST_USER     = 'avisos@conserte.me'
EMAIL_HOST_PASSWORD = 'Mj?*j!6m'
DEFAULT_FROM_EMAIL  = 'avisos@conserte.me'
SERVER_EMAIL        = 'avisos@conserte.me'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True

APPEND_SLASH = True

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'

LOGOUT_REDIRECT_URL = '/'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = BASE_ROOT + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = BASE_ROOT + '/assets/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/assets/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_ROOT + '/static/assets/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 's#_3ozw)&amp;(h+2=^t26h1w&amp;z47!pd#0ptsz!*+&amp;nex7vsul_o&amp;i'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'hamlpy.template.loaders.HamlPyFilesystemLoader',
    'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'conserte_me.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'conserte_me.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_ROOT + '/templates',
    BASE_ROOT + '/profiles',
    '/home/conserte_me/website/conserte_me',
    '/home/conserte_me/website/issues',
    '/home/conserte_me/website/templates',
)

# TEMPLATE_CONTEXT_PROCESSORS = 'django.contrib.messages.context_processors.messages'
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.comments',

    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.staticfiles',

    # thumbs
    'easy_thumbnails',

    # migrations
    'south',

    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'conserte_me',
    'issues',
    'profiles',

    # plugins
    'rest_framework',

    # custom comments
    # 'issue_comments',
)

# Custom comment application
# COMMENTS_APP = 'issue_comments'


THUMBNAIL_ALIASES = {
    '': {
        'square': {'size': (50, 50), 'crop': 'smart'},
        'big_square': {'size': (100, 100), 'crop': 'smart'},
        'medium': {'size': (250, 250), 'crop': False},
        'big':    {'size': (500, 500), 'crop': False},
    },
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# setup logger
import logging
PROJECT_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(PROJECT_DIR)
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename=os.path.join(PARENT_DIR, 'django.log'),
    filemode='a+')
