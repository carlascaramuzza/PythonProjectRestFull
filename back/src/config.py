class DevelopmentConfig():
    DEBUG = True
    SECRET_KEY = 'senhabraba'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'dev465'
    MYSQL_DB = 'restaurante'

config ={
    'development': DevelopmentConfig
}