from flask_mail import Message

from App.exts import mail
from App.mail_code_uitls import verification_code


def SendMail(email):
    email_list=[]
    email_list.append(email)
    msg = Message('经济数学教学平台验证码', sender='life_need_python@163.com', recipients=email_list)
    msg.body=verification_code()
    # msg.html='<h1>kkk</h1>'
    code=msg.body
    mail.send(msg)
    return code
