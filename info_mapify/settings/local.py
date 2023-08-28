from .base import *
from dotenv import load_dotenv


load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'info_mapify',
        'USER': 'postgres',
        'PASSWORD': 'martiseva2003',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
