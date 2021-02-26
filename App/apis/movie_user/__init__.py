from flask_restful import Api

from App.apis.movie_user.movie_order_api import MovieOrderResource, MovieOrdersResource
from App.apis.user.login_api import UserResource

user_movie_api=Api(prefix='/user')

user_movie_api.add_resource(MovieOrdersResource,'/movieuser/')
user_movie_api.add_resource(MovieOrderResource,'/movieuser/<int:order_id>/')