from flask import g
from flask_restful import Resource, fields, marshal_with, reqparse, abort

from App.apis.user.models_utils import get_user
from App.exts import cache
from App.send_mail import SendMail
global send_mail_code
parser_code = reqparse.RequestParser()
parser_code.add_argument('user', type=str, required=True, help='请输入用户')
class FindCodeResource(Resource):
    def post(self):
        args = parser_code.parse_args()
        users = args.get('user')
        user = get_user(users)
        if not user:
            abort(400, msg='用户不存在')
        if user.is_delect != False:
            print(user.is_delect)
            abort(400, msg='用户不存在')
        try:
            send_mail_code=SendMail(user.email)
        except:
            abort(403, msg='没有这个邮箱')
        print(send_mail_code)
        if cache.get('codeforget'):
            cache.delete('codeforget')
        cache.set('codeforget', send_mail_code.lower(), timeout=61)
        data = {'msg': '验证码发送成功',
                'status': 201}
        return data


