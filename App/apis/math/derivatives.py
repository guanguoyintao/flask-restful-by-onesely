from flask_restful import abort
from sympy import symbols, diff, latex


def Derivatives(function,order,var_s):
    s_expr = ''
    try:
        s_expr_dict = {}
        x = 0
        y = 0
        z = 0
        a = 0
        b = 0
        c = 0
        e = 0
        f = 0
        g = 0
        h = 0
        ii = 0
        j = 0
        str1 = [x, y, z, a, b, c, e, f, g, h, ii, j]
        l2 = var_s.split()
        l1 = list(set(l2))
        lis = []
        print(l1)
        if len(l2) != len(l1):
            abort(401, msg='输入自变量重复')
        else:
            for i in range(len(l1)):
                str1[i] = symbols(l1[i])
                lis.append(str1[i])
            ab = function
            print(lis)
            if len(l1) > 1:
                for i in range(len(l1)):
                    s_expr_dict[l1[i]] = diff(ab, str1[i])
                print(s_expr_dict)
                if order == '1':
                    s_expr = latex(diff(ab, lis))
                    print(s_expr)
                elif order == '2':
                    s_expr = latex(diff(diff(ab, lis), lis))
                    print(s_expr)
                elif order == '3':
                    s_expr = latex(diff(diff(diff(ab, lis), lis), lis))
                    print(s_expr)
                elif order == '4':
                    s_expr = latex(diff(diff(diff(diff(ab, lis), lis), lis), lis))
                    print(s_expr)
                elif order == '5':
                    s_expr = latex(diff(diff(diff(diff(diff(ab, lis), lis), lis), lis), lis))
                    print(s_expr)
            elif len(l1) == 1:
                if order == '1':
                    s_expr = latex(diff(ab, str1[0]))
                    print(s_expr)
                elif order == '2':
                    s_expr = latex(diff(diff(ab, str1[0]), str1[0]))
                    print(s_expr)
                elif order == '3':
                    s_expr = latex(diff(diff(diff(ab, str1[0]), str1[0]), str1[0]))
                    print(s_expr)
                elif order == '4':
                    s_expr = latex(diff(diff(diff(diff(ab, str1[0]), str1[0]), str1[0]), str1[0]))
                    print(s_expr)
                elif order == '5':
                    s_expr = latex(
                        diff(diff(diff(diff(diff(ab, str1[0]), str1[0]), str1[0]), str1[0]), str1[0]))
                    print(s_expr)
        return s_expr
    except:
        abort(401, msg='输入格式不对')
        return s_expr