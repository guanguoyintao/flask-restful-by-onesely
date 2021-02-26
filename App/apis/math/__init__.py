from flask_restful import Api

from App.apis.admin.admin_api import AdminResource
from App.apis.admin.admin_code_api import AdminCodeResource


admin_api=Api(prefix='/user')

admin_api.add_resource(AdminResource,'/admin/')
admin_api.add_resource(AdminCodeResource,'/admincode/')