from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'p-enterprise.com',
        'NAME': 'cci_db',
        'USER': 'root',
        'PASSWORD': 'cci@dm1n',
        'PORT': '9200',
        'OPTIONS': {
            "init_command": "SET storage_engine=MYISAM",
        }
    }
}
