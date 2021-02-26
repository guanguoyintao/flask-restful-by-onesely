from flask_restful import abort
from sympy import symbols, latex, integrate


def Definite_integral(function,var_s,a,b):
    s_expr = ''
    try:
        if len(var_s) != 1:
            abort(401, msg='输入自变量重复')
        elif len(var_s) > 1:
            abort(401, msg='输入自变量过多')
        else:
            x = symbols(var_s)
            ab = function
            if len(var_s) == 1:
                s_expr = latex(integrate(ab, (x, a, b)))
                print(s_expr)
        return s_expr
    except:
        abort(401, msg='输入格式不对')
        return s_expr