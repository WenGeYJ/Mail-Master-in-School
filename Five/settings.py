# -*- coding: UTF-8 -*-
"""
Django settings for Five project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vr62)fr)j@nh2%v+wz8qyb4j%el_z8u0k5ve@1!*ogk1s9vm3!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',

    'el_pagination',
    'easy_thumbnails',
    'constance',
    'constance.backends.database',
    'djangobower',

    'lbforum',
    'lbattachment',
    'lbutils',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Five.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Five.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # or mysql.connector.django
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST':'localhost',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#配置失效时间为半个小时
SESSION_COOKIE_AGE = 60*30
#关闭浏览器清除cookie
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


HOST_URL = ''
MEDIA_URL_ = '/media/'
MEDIA_URL = HOST_URL + MEDIA_URL_
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SIGNUP_URL = '/regist/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'
CHANGE_PASSWORD_URL = '/accounts/password/change/'

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'forbidden_words': ('', 'Forbidden words', str),
}

from django.conf.global_settings import STATICFILES_FINDERS
STATICFILES_FINDERS += (('djangobower.finders.BowerFinder'),)

BOWER_COMPONENTS_ROOT = BASE_DIR

BOWER_INSTALLED_APPS = (
    'jquery#1.12',
    'markitup#1.1.14',
    'mediaelement#2.22.0',
    'blueimp-file-upload#9.12.5',
)

BBCODE_AUTO_URLS = True
#add allow tags
HTML_SAFE_TAGS = ['embed']
HTML_SAFE_ATTRS = ['allowscriptaccess', 'allowfullscreen', 'wmode']
#add forbid tags
HTML_UNSAFE_TAGS = []
HTML_UNSAFE_ATTRS = []
LBFORUM_TITLE = "forum"
LBFORUM_SUB_TITLE = "subforum"
"""
#default html safe settings
acceptable_elements = ['a', 'abbr', 'acronym', 'address', 'area', 'b', 'big',
    'blockquote', 'br', 'button', 'caption', 'center', 'cite', 'code', 'col',
    'colgroup', 'dd', 'del', 'dfn', 'dir', 'div', 'dl', 'dt', 'em',
    'font', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
    'ins', 'kbd', 'label', 'legend', 'li', 'map', 'menu', 'ol',
    'p', 'pre', 'q', 's', 'samp', 'small', 'span', 'strike',
    'strong', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
    'thead', 'tr', 'tt', 'u', 'ul', 'var']
acceptable_attributes = ['abbr', 'accept', 'accept-charset', 'accesskey',
    'action', 'align', 'alt', 'axis', 'border', 'cellpadding', 'cellspacing',
    'char', 'charoff', 'charset', 'checked', 'cite', 'clear', 'cols',
    'colspan', 'color', 'compact', 'coords', 'datetime', 'dir',
    'enctype', 'for', 'headers', 'height', 'href', 'hreflang', 'hspace',
    'id', 'ismap', 'label', 'lang', 'longdesc', 'maxlength', 'method',
    'multiple', 'name', 'nohref', 'noshade', 'nowrap', 'prompt',
    'rel', 'rev', 'rows', 'rowspan', 'rules', 'scope', 'shape', 'size',
    'span', 'src', 'start', 'summary', 'tabindex', 'target', 'title', 'type',
    'usemap', 'valign', 'value', 'vspace', 'width', 'style']
"""