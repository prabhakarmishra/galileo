"""
WSGI config for ipad_byod project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os,sys
from site import addsitedir
# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

WSGIPythonPath = '/usr/local/lib/python2.7/site-packages'
addsitedir('/usr/local/lib/python2.7/site-packages/')
#os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studentgrind.settings")

sys.path.append('/var/www/user1/www/studentgrind/')
sys.path.append('/var/www/user1/www/studentgrind/studentgrid/')

path = PROJECT_ROOT
if path not in sys.path:
    sys.path.append(path)
#sys.path.append(r"/var/www/user1/www/studentgrind")


# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

