import uuid

from flask import g
from flask_restful import abort, fields, marshal, marshal_with, reqparse

from App.apis.base_resource import TabrResource
from App.apis.user.models_utils import get_user
from App.exts import cache



find_user= reqparse.RequestParser()

find_user.add_argument('user', type=str, required=True, help='请输入用户')

find_user.add_argument('code', type=str, required=True, help='请确认验证码')



class FindUserResource(TabrResource):
    # @marshal_with(single_users_fields)
    def post(self):
        args = find_user.parse_args()
        users = args.get('user')
        print(users)
        codes = args.get('code').lower()
        if not cache.get('codeforget'):
            abort(400, msg='请获取验证码')
        code = cache.get('codeforget')
        print(code)
        if not code == codes:
            abort(400, msg='验证码错误')
        user = get_user(users)
        if not user:
            abort(400, msg='用户不存在')
        if user.is_delect != False:
            print(user.is_delect)
            abort(400, msg='用户不存在')
        cache.set('userid', user.email, timeout= 60 * 24)
        data = {'msg': '确认用户成功',
                'status': 201}
        return data

