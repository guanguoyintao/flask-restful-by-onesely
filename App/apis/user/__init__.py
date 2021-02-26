from flask_restful import Api

from App.apis.user.code_api import CodeResource
from App.apis.user.login_api import UserResource

user_api=Api(prefix='/user')

user_api.add_resource(UserResource,'/user/')
user_api.add_resource(CodeResource,'/code/')