"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
apps_path = os.path.join(BASE_DIR, 'apps')
sys.path.append(apps_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i0qni7v#62jzmn04%g3#l-*3t^)0=p0r$n%*r=(3zf8usu7mj9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'home',
    'user'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'home.middleware.CORSMiddele'
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
res = os.getenv('DB_PWD', '123')
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'POST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '123',
        'PORT': 3306,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            # ????????????????????????WARNING
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            # ????????????????????????ERROR
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            # ????????????,???????????????,???????????????????????????????????????????????????????????????????????????BASE_DIR???????????????luffyapi
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs", "luffy.log"),
            # ????????????????????????,??????????????????300M
            'maxBytes': 300 * 1024 * 1024,
            # ?????????????????????,???????????????????????????10
            'backupCount': 10,
            # ????????????:????????????
            'formatter': 'verbose',
            # ??????????????????
            'encoding': 'utf-8'
        },
    },
    # ????????????
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,  # ???????????????????????????????????????????????????????????????
        },
    }
}

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'utils.exception.common_exception_handler',
}

# media?????????
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# ???????????????dev?????????
AUTH_USER_MODEL = 'user.user'

# ????????????

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
    'token',
)

from .common_settings import *

# simpleui??????

import time

SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menu_display': ['????????????', '????????????', '??????'],  # ???????????????????????????, ?????????????????????????????????????????????, ?????????[] ??????????????????.
    # 'menu_display': ['????????????',  '????????????', '??????????????????','??????????????????'],      # ???????????????????????????, ?????????????????????????????????????????????, ?????????[] ??????????????????.
    'dynamic': True,  # ??????????????????????????????, ?????????False. ????????????, ??????????????????????????????????????????????????????
    'menus': [
        {
        'name': '????????????',
        'icon': 'fab fa-apple',
        'url': '/backend/'
        },
        {
        'app': 'auth',
        'name': '????????????',
        'icon': 'fas fa-user-shield',
        'models': [
            {
                'name': '??????',
                'icon': 'fa fa-user',
                'url': 'auth/user/'
            },
            {
                'name': '???',
                'icon': 'fa fa-user',
                'url': 'auth/group/'
            },
            {
                'name': '??????',
                'icon': 'fa fa-user',
                'url': 'auth/permission/'
            }

        ]
    },
        {
        'app': 'home',
        'name': '??????',
        'icon': 'fas fa-user-shield',
        'models': [
            {
                'name': '?????????',
                'icon': 'fa fa-user',
                'url': 'home/banner/'
            }

        ]
    }
        #     {
        #     # ???2021.02.01+ ?????????????????????models ???????????????
        #     'name': '??????????????????',
        #     'icon': 'fa fa-file',
        #   	# ????????????
        #     'models': [{
        #         'name': 'Baidu',
        #         'icon': 'far fa-surprise',
        #         # ??????????????? ???
        #         'models': [
        #             {
        #               'name': '?????????',
        #               'url': 'https://www.iqiyi.com/dianshiju/'
        #               # ???????????????????????????element????????????3???
        #             }, {
        #                 'name': '????????????',
        #                 'icon': 'far fa-surprise',
        #                 'url': 'https://zhidao.baidu.com/'
        #             }
        #         ]
        #     }, {
        #         'name': '????????????',
        #         'url': 'https://www.wezoz.com',
        #         'icon': 'fab fa-github'
        #     }]
        # },
        #     {
        #     'name': '??????????????????' ,
        #     'icon': 'fa fa-desktop',
        #     'models': [{
        #         'name': time.time(),
        #         'url': 'http://baidu.com',
        #         'icon': 'far fa-surprise'
        #     }]
        # }
    ]
}
SIMPLEUI_HOME_INFO = False