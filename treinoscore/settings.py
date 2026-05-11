import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-7*be7+u&7_c_pz_-ok5x43_ki#@tgu8-9uf)%r7mc%n%z&hfqj'

DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'workouts',
    'core',
    'bootstrap4',
]

JAZZMIN_SETTINGS = {
    "site_title": "TreinoScore Admin",
    "site_header": "TreinoScore",
    "site_brand": "TreinoScore",
    "welcome_sign": "Bem-vindo ao TreinoScore Admin",
    "copyright": "TreinoScore Ltd",
    "search_model": ["auth.User"],
    "topmenu_links": [
        {"name": "Home", "url": "admin:index",
            "permissions": ["auth.view_user"]},
    ],
}

JAZZMIN_UI_SETTINGS = {
    "theme": "slate",
    "dark_mode_theme": "darkly",
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'treinoscore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'treinoscore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases


# TreinoScore_django
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "TreinoScore_django",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# AUTH_USER_MODEL = ''
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'


# configurações de email
# abaixo o código para simular o envio de email, printando no console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

'''
Configuração quando se tem server de email
se informa:
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'no-replay@seudominio.com.br (email que conecta no servidor)
EMAIL_PORT = 586 (Ou a que o servidor informar)
EMAIL_USE_TSL = True (Se vai utilizar criptografia ou não)
EMAIL_HOST_PASSWORD = 'sua-senha'
'''
