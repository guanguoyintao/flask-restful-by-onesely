from flask import g
from flask_restful import Resource, fields, reqparse, marshal_with, abort

from App.exts import cache
from App.send_mail import SendMail
global send_mail_code
admin_parser_code = reqparse.RequestParser()
admin_parser_code.add_argument('g_email', type=str, required=True, help='请输入邮箱')
class AdminCodeResource(Resource):
    def post(self):
        args = admin_parser_code.parse_args()
        email = args.get('g_email')
        try:
            send_mail_code=SendMail(email)
        except:
            abort(403, msg='没有这个邮箱')
        print(send_mail_code)
        if cache.get('admincode'):
            cache.delete('admincode')
        cache.set('admincode', send_mail_code, timeout=61)
        data = {'msg': '验证码发送成功',
                'status': 201}
        return data


