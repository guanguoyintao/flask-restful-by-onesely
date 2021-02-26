from flask_restful import abort
from sympy import latex

from App.apis.math import math_exp


def Fraction(function):
    s_expr = ''
    try:
        s_expr = latex(math_exp.main(function))
        print(s_expr)
        return s_expr
    except:
        abort(401, msg='输入格式不对')
        return s_expr