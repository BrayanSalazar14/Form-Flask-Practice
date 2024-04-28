class Config:
    SECRET_KEY = "B!1weNAt1T^%kvhUI*S"


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'brayan'
    MYSQL_PASSWORD = '12345'
    MYSQL_DB = "flask_login"


config = {
    'development': DevelopmentConfig
}
