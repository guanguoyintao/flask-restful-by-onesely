from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache


db = SQLAlchemy()
migrate=Migrate()
mail=Mail()
cache=Cache(
config={
        'CACHE_TYPE': 'redis'
        # 'CACHE_REDIS_HOST': '127.0.0.1',
        # 'CACHE_REDIS_PORT': 6379,
        # 'CACHE_REDIS_DB': 1
    }
)
def init_ext(app):
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    cache.init_app(app)