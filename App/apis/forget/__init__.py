from flask_restful import Api

from App.apis.forget.code_forget_api import FindCodeResource
from App.apis.forget.find_user_api import FindUserResource
from App.apis.forget.upgrade_user_api import UpgradeUserResource

forget_user_api=Api(prefix='/user')

forget_user_api.add_resource(FindUserResource,'/forgetuser/')
forget_user_api.add_resource(FindCodeResource,'/forgetcode/')
forget_user_api.add_resource(UpgradeUserResource,'/forget/')