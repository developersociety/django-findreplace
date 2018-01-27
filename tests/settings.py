from __future__ import unicode_literals

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

SECRET_KEY = 'findreplace'

INSTALLED_APPS = [
    'findreplace',
    'tests',
]
