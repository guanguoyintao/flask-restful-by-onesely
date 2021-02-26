import functools

from flask_restful import abort
def Factorial(number):
    s_expr=''
    try:
        if number != '':
            s_expr = str((lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(int(number)))

            print(s_expr)
        elif number == '':
            abort(401, msg='未输入数字')
        return s_expr
    except:
        abort(401, msg='输入格式不对')
        return s_expr

