SECRET_KEY = 'i0_+-t@@wul&q)30+4y)8-19s)31@%cv8$q(c@8q1g#h$6wn-='

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

## Thumbor ##
THUMBOR_SERVER = 'http://localhost:8888'
THUMBOR_WRITABLE_SERVER = THUMBOR_SERVER
#THUMBOR_MEDIA_URL = 'http://localhost:8000/media'
THUMBOR_SECURITY_KEY = 'MY_SECURE_KEY'