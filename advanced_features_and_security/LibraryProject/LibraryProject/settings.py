from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6v(7bps5pk3%ywp)c)4+k=(7x+*yr14-s$9#jab0*_0kf1*5fa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Change to False in production

ALLOWED_HOSTS = []  # Specify allowed hosts

AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware must be enabled
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===================================
# SECURITY CONFIGURATIONS (Added)
# ===================================

SECURE_BROWSER_XSS_FILTER = True  # Protects against XSS attacks
X_FRAME_OPTIONS = 'DENY'  # Prevents Clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME-type sniffing

# Secure cookies
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookies are sent only over HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookies are sent only over HTTPS

# HTTPS-related settings
SECURE_SSL_REDIRECT = True  # Redirects HTTP to HTTPS
SECURE_HSTS_SECONDS = 31536000  # Enables HTTP Strict Transport Security for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Applies HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allows HSTS preloading in browsers

