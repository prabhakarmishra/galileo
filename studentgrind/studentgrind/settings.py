# Django settings for studentgrind project.
import os
from os import path
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Rahul Kumar', 'rahulkumar.k2007@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'studentgrind',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'root@420',                  # Not used with sqlit3
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

##get dynamic path according to project location

ALLOWED_HOST = ['54.218.113.201']

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT ='/var/www/user1/www/studentgrind/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL =''# '54.218.113.201/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT ='/var/www/user1/www/studentgrind/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL ='/static/' #'54.218.113.201/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

##Custom date formating
DATE_INPUT_FORMATS = ('%Y-%m-%d',
 '%m-%d-%Y',
 '%m/%d/%Y',
 '%m/%d/%y',
 '%b %d %Y',
 '%b %d, %Y',
 '%d %b %Y',
 '%d %b, %Y',
 '%B %d %Y',
 '%B %d, %Y',
 '%d %B %Y',
 '%d %B, %Y'
)
DATETIME_INPUT_FORMATS = (
'%Y-%m-%d %H:%M:%S',
 '%Y-%m-%d %H:%M:%S.%f',
 '%Y-%m-%d %H:%M',
 '%Y-%m-%d',
 '%m-%d-%Y',
 '%m/%d/%Y %H:%M:%S',
 '%m/%d/%Y %H:%M:%S.%f',
 '%m/%d/%Y %H:%M',
 '%m/%d/%Y',
 '%m/%d/%y %H:%M:%S',
 '%m/%d/%y %H:%M:%S.%f',
 '%m/%d/%y %H:%M',
 '%m/%d/%y'
)

TIME_INPUT_FORMATS = ['%H:%M', '%I:%M%p', '%I:%M %p']
# Additional locations of static files
STATICFILES_DIRS = (
	'/var/www/user1/www/studentgrind/static',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

FILE_UPLOAD_MAX_MEMORY_SIZE = "5242880"
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'moq^mcpfh3am)k896sxrdw8!n69zfkd$$iq231vh$+*n47czz_'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
   # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
	'social_auth.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'studentgrind.urls'

WSGI_APPLICATION = 'studentgrind.wsgi.application'

EMAIL_HOST='localhost'
EMAIL_PORT='25'


TEMPLATE_DIRS = (
	'/var/www/user1/www/studentgrind/templates',

    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	
)

TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.request',
 'django.contrib.auth.context_processors.auth',
 'social_auth.context_processors.social_auth_by_name_backends',
 'social_auth.context_processors.social_auth_backends',
 'social_auth.context_processors.social_auth_by_type_backends',
 'social_auth.context_processors.social_auth_login_redirect',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'piston',
    'alpha',
	'social_auth',

    #'south',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

AUTHENTICATION_BACKENDS = (
    #'emailusernames.backends.EmailAuthBackend',
    # 'django.contrib.auth.backends.ModelBackend',
    # add the social_auth authentication backend. We're not using the default
    # ModelBackend, but if you are, leave it in the list.
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
)
LINKEDIN_CONSUMER_KEY = 'feu39xo1i87q' # linkedin calls this the "API Key"
LINKEDIN_CONSUMER_SECRET = 'aPgYYYQ2eDDd4IR4' # "Secret Key"

LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress', 'r_fullprofile']
LINKEDIN_EXTRA_FIELD_SELECTORS = [
    'email-address',
    'headline',
    'industry',
    'location',
    'summary',
    'specialties',
    'positions',
    'educations',
    'skills',
    'summary',
]

LINKEDIN_EXTRA_DATA = [('id', 'id'),
                       ('first-name', 'first_name'),
                       ('last-name', 'last_name'),] + [
                           (field, field.replace('-', '_'), True)
                           for field in LINKEDIN_EXTRA_FIELD_SELECTORS
                       ]

SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/talent/new/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = SOCIAL_AUTH_NEW_USER_REDIRECT_URL
LOGIN_ERROR_URL = '/error/'
LOGIN_URL = "/login/"	
SOCIAL_AUTH_BACKEND_ERROR_URL = '/error/'				   
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
         # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': PROJECT_ROOT + "/logfile",
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'alpha': {
            'handlers': ['logfile'],
            'level': 'DEBUG', # Or maybe INFO or DEBUG
            'propogate': False,
        },
    }
}
