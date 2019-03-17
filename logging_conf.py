# coding=utf-8

from Utilities import setting as S
from logging import config
import logging

# 'format': '%(asctime)s - %(name)s - %(levelname)s - %(pathname)s - %(lineno)d - %(message)s'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
            'filename': S.LOG_NAME + '.log',
            'mode': 'a'
        }
    },

    'loggers': {
        S.LOG_NAME: {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}

config.dictConfig(LOGGING)



