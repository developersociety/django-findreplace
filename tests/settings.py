DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

USE_TZ = True

SECRET_KEY = "findreplace"

INSTALLED_APPS = ["findreplace", "tests"]
