import uuid

from flask import g
from flask_restful import abort, fields, marshal, marshal_with, reqparse

from App.apis.base_resource import TabrResource
from App.apis.user.models_utils import get_user
from App.exts import cache, db

upgrade_password= reqparse.RequestParser()

upgrade_password.add_argument('password', type=str, required=True, help='请输入密码')
# upgrade_password.add_argument('user', type=str, required=True, help='请输入用户')




class UpgradeUserResource(TabrResource):
    # @marshal_with(single_users_fields)
    def post(self):
        args = upgrade_password.parse_args()
        password = args.get('password')
        if not cache.get('userid'):
            abort(400, msg='没有用户')
        user_email = cache.get('userid')
        # print(user_email)
        user = get_user(user_email)
        if not user:
            abort(400, msg='用户不存在')
        if user.is_delect != False:
            print(user.is_delect)
            abort(400, msg='用户不存在')
        user._password = password
        # db.session.commit()
        # if not db.session.commit():
        #     abort(400, msg='fail')
        print(password)
        user.save()

        if not  user.save():
            abort(400, msg='fail')
        data = {'msg': '密码重置成功',
                'status': 201}
        return data
#pbkdf2:sha256:150000$5xICkvUm$b11ca80d8e14507f10b4ef2e33e16f7ef8e34414e67680ba588dff12e75f9c19
#$2aba3a770a4ffcd2b655e2f44259d3671bbe33b832c1bb0bcf6c5782d82f1c31