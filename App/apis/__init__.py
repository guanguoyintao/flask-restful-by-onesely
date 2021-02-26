from flask_restful import Api

from App.apis.admin import admin_api
from App.apis.forget import forget_user_api
from App.apis.movie_user import user_movie_api
from App.apis.user import user_api


def init_api(app):
    forget_user_api.init_app(app)
    admin_api.init_app(app)
    user_api.init_app(app)
