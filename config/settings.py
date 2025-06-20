# settings.py (수정 완료된 버전)

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# !!! 중요 !!! 이 아래 라인은 원래 파일에 있던 본인의 실제 SECRET_KEY 값으로 꼭 다시 바꿔주세요!
SECRET_KEY = 'django-insecure-5*&fhneexe4c*3l8lx_5=_o6_3^+i2jrpu=x+*hq+lve&i=jbd'


# 1. 보안을 위해 DEBUG는 False로 변경했습니다.
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# 2. ALLOWED_HOSTS는 그대로 유지합니다.
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'aa0313.pythonanywhere.com', '현금화.site']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django