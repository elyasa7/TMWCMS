import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/turkmenweb/turkmenweb/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/turkmenweb/turkmenweb/bin')
sys.path.append('/home/turkmenweb/turkmenweb/bin/turkmenweb')
sys.path.append('/home/turkmenweb/turkmenweb/bin/turkmenweb/static')
sys.path.append('/home/turkmenweb/turkmenweb/bin/turkmenweb/turkmenweb')

# Activate your virtual env
activate_env=("/home/turkmenweb/turkmenweb/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'turkmenweb.settings'
application = get_wsgi_application()