# Local imports
from .base import *

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

DEBUG = True

# Applications from base + local
INSTALLED_APPS += [
    # Third-party apps
    'django_extensions',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
