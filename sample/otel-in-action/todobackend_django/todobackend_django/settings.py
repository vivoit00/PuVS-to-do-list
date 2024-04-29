from django.core.management.utils import get_random_secret_key

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'todobackend_django.urls' 

SECRET_KEY = get_random_secret_key()

INSTALLED_APPS = [
    
    'rest_framework',
    'todos',
    
]

#DATABASES: {}
