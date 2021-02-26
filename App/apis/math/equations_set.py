from flask_restful import abort
from sympy import solve


def Equations_set(function):
    if function != '':
        try:
            s_expr1 = function.strip(';').split(';')
            for i in s_expr1:
                if ' ' in s_expr1:
                    s_expr1.remove(' ')
            s_e = solve(s_expr1)
            for key in s_e:
                s_expr = s_expr + str(key) + ':' + str(s_e[key]) + '\n'
            print(s_expr)
        except:
            abort(401, msg='输入格式不对')