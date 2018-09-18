

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0,os.path.join(BASE_DIR,'apps'))



SECRET_KEY = '!a_im^j%zl4z24ci(&d%@3vds(3q!5zf6*#e(s6!*1k*^nwn5h'


DEBUG = True

ALLOWED_HOSTS = []
# 系统app
SYS_APPS=[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',]
# 插件app
EXT_APPS=[
    'xadmin',
    'crispy_forms',
    'reversion',]
# 自建app
MY_APPS=[

    # 首页模块
    'apps.home',
    # 用户模块
    'apps.account',
    # 商品信息模块
    'apps.shop_detail',
    # 分类模块
    'apps.cate_detail',
    # 购物车模块
    'apps.cart',
    # 订单模块
    'apps.order',
    # 支付模块
    'apps.pay',]

INSTALLED_APPS=SYS_APPS+EXT_APPS+MY_APPS


# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'xadmin',
#     'crispy_forms',
#     'reversion',
#     'shop',
# ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TMALL.urls'

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

WSGI_APPLICATION = 'TMALL.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'tmall',
        'USER':'root',
        'PASSWORD':'1314520',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'CHARSET':'utf8'
    }
}




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




LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True




STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),)
    # os.path.join(BASE_DIR,'apps/home/static')

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')