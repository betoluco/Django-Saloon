from website.settings.base import *


ALLOWED_HOSTS = ['192.168.1.3', 'localhost', '127.0.0.1']

DEBUG =True


# Database
DATABASES['default']['NAME'] = 'mvp_db'
DATABASES['default']['USER'] = 'postgres'
DATABASES['default']['PASSWORD'] = 'caf5tl'
