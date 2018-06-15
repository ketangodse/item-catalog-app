import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Auth:
    CLIENT_ID = '1083509420754-cviroif2b3h2t93b9vk64qu3r0patmh7.apps.googleusercontent.com'
    CLIENT_SECRET= 'mFKMke7Ej5yRVEkufxhm0py2'
    REDIRECT_URI= 'https://localhost:5000/gCallback'
    AUTH_URI= 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI= 'https://accounts.google.com/o/oauth2/token'
    USER_INFO='https://www.googleapis.com/userinfo/v2/me'


class Config:
    APP_NAME = 'CatalogApp'
    SECRET_KEY = os.environ.get("SECRET_KEY") or "somethingsecret"

class DevConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI= 'sqlite:///users.db'

class ProdConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI= 'sqlite:///users.db'

config = {
    "dev":DevConfig
    "prod":ProdConfig
    "default":DevConfig
}