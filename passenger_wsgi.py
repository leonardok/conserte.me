import sys, os
 
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + '/conserte_me')

sys.path.insert(0,'/home/conserte_me/env/bin')
sys.path.insert(0,'/home/conserte_me/env/lib/python2.6/site-packages/django')
sys.path.insert(0,'/home/conserte_me/env/lib/python2.6/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "conserte_me.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

