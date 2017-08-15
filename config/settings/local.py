# -*- coding: utf-8 -*-

from .base import *

DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'add_request_info': {
            '()': 'utility.logging.filters.RequestInfoFilter',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['add_request_info'],
            'stream': 'ext://sys.stdout',
            'formatter': 'verbose',
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'encoding': 'utf8',
            'filename': './blog.log',
            'formatter': 'verbose',
            'filters': ['add_request_info'],
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s - %(name)s - '
                      '%(levelname)s[%(request_id)s] - %(message)s',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    },
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'djangoblog', 'static'),
]

