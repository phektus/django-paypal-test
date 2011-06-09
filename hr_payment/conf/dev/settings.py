from hr_payment.conf.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'hr_payment.conf.dev.urls'

MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hr_payment',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}
