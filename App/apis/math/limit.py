from flask_restful import abort
from sympy import symbols, latex


def Limit(function,var_s,limit_type,val):
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
                # limit(f, x, 0, dir='-')
                # {'function': 'x*2', 'var': 'x', 'val': '0', 'answers': '', 'limit_type': 'two-sided',
                # 'return': '1'}
                c = {"two-sided": '', "plus": '+', "minus": '-'}
                print(c[limit_type])
                if c[limit_type] == '':
                    s_expr = latex(limit(ab, x, int(val)))
                    print(s_expr)
                else:
                    print(c[limit_type])
                    s_expr = latex(limit(ab, x, int(val)))
                    print(s_expr)
        return s_expr
    except:
        abort(401, msg='输入格式不对')
        return s_expr