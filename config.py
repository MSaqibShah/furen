class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    DB_NAME = "FRMS"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"
    SQLALCHEMY_DATABASE_URI =f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}'
    # 'mysql+pymysql://DB_USERNAME:DB_PASSWORD@localhost/DB_NAME' 
    IMAGE_UPLOADS = "E:\python\FLASK\P1\app\static\public\img"

    SESSION_COOKIE_SECURE = True

    BCRYPT_LOG_ROUNDS = 12

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "FRMS"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    IMAGE_UPLOADS = "E:\python\FLASK\P1\app\static\public\img"

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    DB_NAME = "FRMS"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    IMAGE_UPLOADS = "E:\python\FLASK\P1\app\static\public\img"

    SESSION_COOKIE_SECURE = False