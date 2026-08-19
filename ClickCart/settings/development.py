import shutil
import tempfile

from .base import *

DEBUG = True
ALLOWED_HOSTS = [
    host.strip()
    for host in config(
        'ALLOWED_HOSTS',
        default='.vercel.app,localhost,127.0.0.1'
    ).split(',')
    if host.strip()
]

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

DATABASE_PATH = os.path.join(BASE_DIR, 'db.sqlite3')
if os.environ.get('VERCEL'):
    DATABASE_PATH = os.path.join(tempfile.gettempdir(), 'clickcart.sqlite3')
    seed_database = os.path.join(BASE_DIR, 'db.sqlite3')
    if os.path.exists(seed_database) and not os.path.exists(DATABASE_PATH):
        shutil.copyfile(seed_database, DATABASE_PATH)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
    }
}

STRIPE_PUBLIC_KEY = config(
    "STRIPE_TEST_PUBLIC_KEY",
    default="pk_test_dummy_key"
)

STRIPE_SECRET_KEY = config(
    "STRIPE_TEST_SECRET_KEY",
    default="sk_test_dummy_key"
)