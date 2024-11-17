# compendio
INSTALLED_APPS = [
    # compendio
    "debug_toolbar",  # ---(1)
]

MIDDLEWARE = [
    # compendio
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # ---(2)
]

INTERNAL_IPS = ['127.0.0.1']  # ---(3)
# compendio