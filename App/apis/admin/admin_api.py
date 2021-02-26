import uuid
from flask_restful import Resource, abort, fields, marshal, marshal_with, reqparse
from App.apis.admin.models_admin_uils import get_admin
from App.apis.api_constant import HTTP_CREATE_OK, HTTP_OK, ADMIN_ACTION_REGISTER, ADMIN_ACTION_LOGIN
from App.exts import cache
from App.models.admin import Admin

users_fields = {
    'name': fields.String,
    'email': fields.String
}
single_users_fields = {
    'data': fields.Nested(users_fields),
    'status': fields.Integer,
    'msg': fields.String,
    'code': fields.String
}
multi_users_fields = {
    'data': fields.List(fields.Nested(users_fields)),
    'status': fields.Integer,
    'msg': fields.String
}
parser_base = reqparse.RequestParser()
parser_base.add_argument('g_password', type=str, required=True, help='请输入密码')
parser_base.add_argument('action', type=str, required=True, help='请确认请求参数')
parser_regieter = parser_base.copy()
parser_regieter.add_argument('g_name', type=str, required=True, help='请输入用户姓名')
parser_regieter.add_argument('g_email', type=str, required=True, help='请输入用户邮箱')
parser_regieter.add_argument('g_code', type=str, required=True, help='请输入验证码')
parser_login = parser_base.copy()
parser_login.add_argument('g_name')
parser_login.add_argument('g_email')


class AdminResource(Resource):
    @marshal_with(multi_users_fields)
    def get(self):
        admin_list = Admin.query.all()
        data = {'msg': 'create success',
                'status': 201,
                'data': admin_list}
        return data

    # @marshal_with(single_users_fields)
    def post(self):
        args = parser_base.parse_args()
        # g_name=request.form.to_dict().get('g_name')
        # g_password = request.form.to_dict().get('g_password')
        # g_email = request.form.to_dict().get('g_email')

        g_password = args.get('g_password')

        action = args.get('action').lower()
        if action == ADMIN_ACTION_REGISTER:
            args_regieter = parser_regieter.parse_args()
            g_name = args_regieter.get('g_name')
            g_email = args_regieter.get('g_email')
            print(g_password)
            admin = Admin()
            admin.name = g_name
            admin.email = g_email
            g_code = args_regieter.get('g_code')
            admin._password = g_password
            if not cache.get('admincode'):
                abort(400, msg='请获取验证码')
            code = cache.get('admincode')
            print(code)
            if not code == g_code:
                abort(400, msg='验证码错误')
            data = {}
            if not admin.save():
                abort(400, msg='fail')
            # 'data':marshal(user,users_fields)
            data = {'msg': 'create success',
                    'status': HTTP_CREATE_OK,
                    'data': admin}
            return marshal(data,single_users_fields)
        elif action == ADMIN_ACTION_LOGIN:
            args_login = parser_login.parse_args()
            g_name = args_login.get('g_name')
            g_email = args_login.get('g_email')

            admin = get_admin(g_name) or get_admin(g_email)
            if not admin:
                abort(400, msg='用户不存在')
            if not admin.check_password(g_password):
                abort(401, msg='密码错误')
            if admin.is_delect != False:
                print(admin.is_delect)
                abort(400, msg='用户不存在')
            token = uuid.uuid4().hex
            print(token)
            cache.set(token, admin.id, timeout=60 * 60 * 24 * 7)
            data1 = {'msg': 'login success',
            'status': HTTP_OK,
            'token': token}
            return data1
        else:
            abort(400, msg='请提供正确的参数')


