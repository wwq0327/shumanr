# -*- coding: utf-8 -*-
"""
Django settings for shumanr project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9e4(9i4ev!8cs9l)v#96d&%hyhhxs6rxox)9kfs)=mfyoc7yf!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ## ------------------------------
    'south',
    'social_auth',
    'linaro_django_pagination',
    ## 'guardian',
    ## ------------------------------
    'markup',
    'blog',
    'profiles',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'linaro_django_pagination.middleware.PaginationMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    'social_auth.context_processors.social_auth_by_type_backends',
)


ROOT_URLCONF = 'shumanr.urls'

WSGI_APPLICATION = 'shumanr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL.replace("/", ""))

MEDIA_URL = '/media/'

# 静态文件目录
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 模版文件目录
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)	

PAGINATION_DEFAULT_PAGINATION = 3

AUTHENTICATION_BACKENDS = (
    ## 'userena.backends.UserenaAuthenticationBackend',
    ## 'guardian.backends.ObjectPermissionBackend',
    ## 'social_auth.backends.contrib.douban.DoubanBackend2',
    'social_auth.backends.contrib.weibo.WeiboBackend',
    'django.contrib.auth.backends.ModelBackend',
)

WEIBO_CLIENT_KEY = '1952908459'
WEIBO_CLIENT_SECRET = 'f66cf7624a0511a9fc56e9ae9fed0f80'

LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'

## SOCIAL_AUTH_PIPELINE = (
##     'social_auth.backends.pipeline.social.social_auth_user',
##     'social_auth.backends.pipeline.associate.associate_by_email',
##     #'social_auth.backends.pipeline.misc.save_status_to_session',
##     'social_auth.backends.pipeline.user.get_username',
##     'social_auth.backends.pipeline.user.create_user',
##     'profiles.pipeline.create_profile', # 自己在accounts這個app下建的pipeline.py
##     'profiles.pipeline.set_guardian_permissions', # 自己在accounts這個app下建的pipeline.py
##     'social_auth.backends.pipeline.social.associate_user',
##     'social_auth.backends.pipeline.social.load_extra_data',
##     'social_auth.backends.pipeline.user.update_user_details',
##     )

## SOCIAL_AUTH_USER_MODEL = 'profiles.Profile'
## ANONYMOUS_USER_ID = -1
## SOCIAL_AUTH_DEFAULT_USERNAME = 'socialauth_user'
