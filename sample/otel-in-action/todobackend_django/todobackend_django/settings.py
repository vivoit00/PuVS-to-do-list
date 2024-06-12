from django.core.management.utils import get_random_secret_key

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'todobackend_django.urls' 

SECRET_KEY = get_random_secret_key()

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'todos',
    
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'postgresdb',
        'PORT': 5432
    }

}

DEBUG = True # For hot reloading

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            # Andere Optionen hier...
        },
    },
]
