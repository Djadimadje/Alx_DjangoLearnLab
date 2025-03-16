# settings.py

import os
from pathlib import Path

# Base settings
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")  # Ensure to set this environment variable securely

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['LibraryProject.com', 'www.LibraryProject.com']

# Application definition
INSTALLED_APPS = [
    # Django apps...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',  # Add any additional apps here
    'bookshelf',  # Your app
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

# CSRF settings
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookie is sent only over HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookie is sent only over HTTPS
CSRF_COOKIE_HTTPONLY = True  # Prevents JavaScript from accessing CSRF cookie

# Security settings
SECURE_BROWSER_XSS_FILTER = True  # Prevents XSS attacks
X_FRAME_OPTIONS = "DENY"  # Prevents clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME sniffing
SECURE_SSL_REDIRECT = True  # Forces redirect to HTTPS
SECURE_HSTS_SECONDS = 31536000  # One year in seconds (for HSTS)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Enable HSTS preload for major browsers
X_CONTENT_TYPE_OPTIONS = "nosniff"  # Prevents MIME sniffing
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS filtering

# Logging (for security events)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django_security.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Update to your DB engine
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Templates settings (Ensure to include csrf token in form templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# Other Django settings
AUTH_PASSWORD_VALIDATORS = [
    # Add any password validation rules you want here
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

# Email settings for secure email handling (use production settings for email)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.your-email-provider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True
