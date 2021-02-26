import os


class Config:
    DEBUG=False
    TESTING=False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/text?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True
    SECRECT_KEY='Rock'
class DevelopConfig(Config):
    DEBUG = False
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'life_need_python@163.com'
    MAIL_PASSWORD = '000139abc'
    # dbinfo={
    #     'DIALECT' : 'mysql',
    # 'DRIVER' : 'pymysql',
    # 'USERNAME' : 'root',
    # 'PASSWORD' :'123456',
    # 'HOST ': '127.0.0.1',
    # 'PORT': '3306',
    # 'DATABASE' : 'text'
    #
    # }
    #
    # SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(dbinfo.get('DIALECT'),
    #                                                                        dbinfo.get('DRIVER'),
    #                                                                        dbinfo.get('USERNAME')
    #                                                                        , dbinfo.get('PASSWORD'),
    #                                                                        dbinfo.get('HOST'),
    #                                                                        dbinfo.get('PORT'),
    #                                                                        dbinfo.get('DATABASE'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
envs={
    'develop':DevelopConfig
}