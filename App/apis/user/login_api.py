import uuid

from flask import g
from flask_restful import abort, fields, marshal, marshal_with, reqparse


from App.apis.api_constant import HTTP_CREATE_OK, USER_ACTION_REGISTER, USER_ACTION_LOGIN, HTTP_OK
from App.apis.base_resource import TabrResource
from App.apis.user.models_utils import get_user
from App.exts import cache
from App.models.user.user import User

users_fields = {
    'name': fields.String,
    'email': fields.String
}
single_users_fields = {
    'data': fields.Nested(users_fields),
    'status': fields.Integer,
    'msg': fields.String,
    'code':fields.String
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
parser_regieter.add_argument('g_code', type=str, required=True, help='请输入验证码')
parser_regieter.add_argument('g_name', type=str, required=True, help='请输入用户姓名')
parser_regieter.add_argument('g_email', type=str, required=True, help='请输入用户邮箱')
parser_login = parser_base.copy()
parser_login.add_argument('g_name')
parser_login.add_argument('g_email')


class UserResource(TabrResource):
    @marshal_with(multi_users_fields)
    def get(self):
        user_list = User.query.all()
        data = {'msg': 'create success',
                'status': 201,
                'data': user_list}
        return data

    # @marshal_with(single_users_fields)
    def post(self):
        args = parser_base.parse_args()
        # g_name=request.form.to_dict().get('g_name')
        # g_password = request.form.to_dict().get('g_password')
        # g_email = request.form.to_dict().get('g_email')

        g_password = args.get('g_password')

        action = args.get('action').lower()
        if action == USER_ACTION_REGISTER:
            args_regieter = parser_regieter.parse_args()
            g_name = args_regieter.get('g_name')
            g_code = args_regieter.get('g_code')
            g_email = args_regieter.get('g_email')
            if not cache.get('code'):
                abort(400, msg='请获取验证码')
            code = cache.get('code')
            print(code)
            if not code == g_code:
                abort(400, msg='验证码错误')
            user = User()
            user.name = g_name
            user.email = g_email
            user._password = g_password
            data = {}
            if not user.save():
                abort(400, msg='fail')
            # 'data':marshal(user,users_fields)
            data = {
                'msg': '创建成功',
                    'status': HTTP_CREATE_OK,
                    'data': user,
                    'code':code}

            return marshal(data,single_users_fields)
        elif action == USER_ACTION_LOGIN:
            args_login = parser_login.parse_args()
            g_name = args_login.get('g_name')
            g_email = args_login.get('g_email')

            user = get_user(g_name) or get_user(g_email)
            if not user:
                abort(400, msg='用户不存在')
            if not user.check_password(g_password):
                abort(401, msg='密码错误')
            if user.is_delect != False:
                print(user.is_delect)
                abort(400, msg='用户不存在')
            token = uuid.uuid4().hex


            print(token)
            cache.set(token, user.id, timeout=60 * 60 * 24)
            data1 = {'msg': '登录成功',
            'status': HTTP_OK,
            'token': token}
            return data1
        else:
            abort(400, msg='请提供正确的参数')


