from flask_restful import abort
from sympy import symbols, integrate, latex


def Indefinite_integralIndefinite_integral(function,var_s):
    s_expr = ''
    try:
        x = 0
        y = 0
        z = 0
        str1 = [x, y, z]
        l1 = list(set(var_s))
        if len(var_s) != len(l1):
            abort(401, msg='输入自变量重复')
        elif len(l1) > 1:
            abort(401, msg='输入自变量过多')
        else:
            for i in range(len(var_s)):
                str1[i] = symbols(l1[i])
            ab = function
            if len(var_s) == 1:
                s_expr = latex(integrate(ab, str1[0]))
                print(s_expr)
        return s_expr
    except:
        abort(401, msg='输入格式不对')
        return s_expr