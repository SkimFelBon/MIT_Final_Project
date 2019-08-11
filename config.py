class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'ithjghosrngosergneorgneorgnerog'
    SQLALCHEMY_DATABASE_URI = "sqlite:///C:/MyPythonScripts/myGitHub/MIT_Final_Project/directory/fix_database.db"

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
