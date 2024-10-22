# Local imports
from .base import *

# Initialize environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = True

# Applications from base + local
INSTALLED_APPS += [
    # Third-party apps
    'django_extensions',
]

# Database SQlite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#Databe postgres.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('USER_DATABASE'),
        'PASSWORD': env('PASSWORD_DATABASE'),
        'HOST': env('HOST_DATABASE'),
        'PORT': env('PORT_DATABASE'),
    }
}
