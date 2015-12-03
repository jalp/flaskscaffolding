import os
import logging


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    LOGGING_FORMAT = '%(asctime)s | %(module)s:%(lineno)d | %(levelname)s | %(message)s'
    LOGGING_LOCATION = 'api.log'
    LOGGING_LEVEL = logging.DEBUG
    DEFAULT_HOST = 'elastic'
    DEFAULT_PORT = 9200


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    DEFAULT_HOST = 'elastic'


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    DEFAULT_HOST = '52.17.247.208'


config = {
    "production": "config.ProductionConfig",
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "default": "config.DevelopmentConfig"
}


def _find_environment():
    ret = 'default'
    config_name = os.getenv('CLOUD_ENVIRONMENT', 'default')
    if config_name in ['scm-dev', 'scm-pre', 'scm-pro']:
        ret = 'production'
    return ret


def configure_app(app):
    app.config.from_pyfile('config.py', silent=True)
    app.config.from_object(config[_find_environment()])
    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
