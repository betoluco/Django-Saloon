from website.settings.base import *


ALLOWED_HOSTS = ['www.celebralize.com']

DEBUG =False


# Database
DATABASES['default']['NAME'] = 'mvp_db'
DATABASES['default']['USER'] = 'super'
DATABASES['default']['PASSWORD'] = 'caf5tl1a774'
DATABASES['default']['HOST'] = 'BETO-207.postgres.pythonanywhere-services.com'
DATABASES['default']['PORT'] = '10207'


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')