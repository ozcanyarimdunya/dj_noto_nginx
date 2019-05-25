import os

from dj_static import MediaCling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = MediaCling(get_wsgi_application())
