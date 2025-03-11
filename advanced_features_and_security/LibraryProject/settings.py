import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your Django apps
    'bookshelf',  # Ensure this app exists in your project
    'relationship_app',  # Ensure this app exists in your project
    'users',  # Add the app where the CustomUser model is located
    'accounts',
]

# Middleware Configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL Configuration
ROOT_URLCONF = 'LibraryProject.urls'

# Templates Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Global templates directory
        'APP_DIRS': True,  # Look for templates in each app's "templates" folder
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

# WSGI Application
WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Authentication Backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
]

# Use the Custom User Model
AUTH_USER_MODEL = 'users.CustomUser'  # Ensure 'users' is the correct app name

# Database Configuration (Make sure this matches your database setup)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Change this if using PostgreSQL or MySQL
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static Files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media Files (User Uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Login and Logout Redirects
LOGIN_REDIRECT_URL = '/'  # Where to redirect after successful login
LOGOUT_REDIRECT_URL = '/login/'  # Fixed cut-off error

# Debugging (Set DEBUG=False in production)
DEBUG = True
ALLOWED_HOSTS = ['*']  # Allow all hosts (Change in production)

