"""Setting up all logs."""
#
import logging.config

logging_settings = {
    "version": 1,
    "formatters": {
        "default_formatter": {
            "format": "%(asctime)s - %(name)s - %(message)s"
        },
    },
    "handlers": {
        "handler_sample": {
            "class": "logging.FileHandler",
            "formatter": "default_formatter",
            "filename": "logs/logging_sample.log"
        },
    },
    "loggers": {
        "dp189.tests.logging_sample": {
            "handlers": ["handler_sample"],
            "level": "DEBUG"
        },
    },
}

logging.config.dictConfig(logging_settings)
