from flask import g
from flask_restful import Resource, fields, marshal_with, reqparse, abort
from App.exts import cache
from App.send_mail import SendMail
global send_mail_code
parser_code = reqparse.RequestParser()
parser_code.add_argument('g_email', type=str, required=True, help='请输入邮箱')
class CodeResource(Resource):
    def post(self):
        args = parser_code.parse_args()
        email = args.get('g_email')
        try:
            send_mail_code=SendMail(email)
        except:
            abort(403, msg='没有这个邮箱')
        print(send_mail_code)
        if cache.get('code'):
            cache.delete('code')
        cache.set('code', send_mail_code, timeout=61)
        data = {'msg': '验证码发送成功',
                'status': 201}
        return data


