from flask_restful import abort
import numpy as np

def Matrix(matrix1,matrix2,add,sub,multi):
    s_expr = ''
    try:
        if matrix1 != '' and matrix2 != '' and (
                add == 'on' or sub == 'on' and multi == 'on'):
            if add == 'on':
                    s_expr1 = matrix1.strip(';').split(';')
                    for i in s_expr1:
                        if ' ' in s_expr1:
                            s_expr1.remove(' ')
                    c = [i.strip(' ').split(' ') for i in s_expr1]
                    for i in range(len(c)):
                        for j in range(c[i].count('')):
                            print(c[i].remove(''))
                        for z in range(len(c[i])):
                            c[i][z] = int(c[i][z])
                    a1 = np.array(c)
                    s_expr2 = matrix2.strip(';').split(';')
                    for i in s_expr2:
                        if ' ' in s_expr2:
                            s_expr2.remove(' ')
                    c2 = [i.strip(' ').split(' ') for i in s_expr2]
                    for i in range(len(c2)):
                        for j in range(c2[i].count('')):
                            print(c2[i].remove(''))
                        for z in range(len(c2[i])):
                            c2[i][z] = int(c2[i][z])
                    a2 = np.array(c2)
                    s_expr3 = a1 + a2
                    #     将矩阵解码为字符串
                    n, m = s_expr3.shape
                    s_expr = '加法结果\n'
                    for i in range(n):
                        for j in range(m):
                            s_expr = s_expr + ' ' + str("%.2f" % s_expr3[i][j])
                            if j == m - 1:
                                s_expr = s_expr + ';\n'
            else:
                s_expr = ''
            # {'matrix1': '1234', 'matrix2': '1244', 'add': 'on', 'sub': 'on', 'multi': 'on', 'return': '1'}
                if sub == 'on':
                    s_expr1 = matrix1.strip(';').split(';')
                    for i in s_expr1:
                        if ' ' in s_expr1:
                            s_expr1.remove(' ')
                    c = [i.strip(' ').split(' ') for i in s_expr1]
                    for i in range(len(c)):
                        for j in range(c[i].count('')):
                            print(c[i].remove(''))
                        for z in range(len(c[i])):
                            c[i][z] = int(c[i][z])
                    a1 = np.array(c)
                    s_expr2 = matrix2.strip(';').split(';')
                    for i in s_expr2:
                        if ' ' in s_expr2:
                            s_expr2.remove(' ')
                    c2 = [i.strip(' ').split(' ') for i in s_expr2]
                    for i in range(len(c2)):
                        for j in range(c2[i].count('')):
                            print(c2[i].remove(''))
                        for z in range(len(c2[i])):
                            c2[i][z] = int(c2[i][z])
                    a2 = np.array(c2)
                    s_expr3 = a1 - a2
                    #     将矩阵解码为字符串
                    n, m = s_expr3.shape
                    s_expr = s_expr + '\n ' + '减法结果\n'
                    for i in range(n):
                        for j in range(m):
                            s_expr = s_expr + ' ' + str("%.2f" % s_expr3[i][j])
                            if j == m - 1:
                                s_expr = s_expr + ';\n'
                else:
                    s_expr = s_expr + ''
            if multi == 'on':
                    s_expr1 = matrix1.strip(';').split(';')
                    for i in s_expr1:
                        if ' ' in s_expr1:
                            s_expr1.remove(' ')
                    c = [i.strip(' ').split(' ') for i in s_expr1]
                    for i in range(len(c)):
                        for j in range(c[i].count('')):
                            print(c[i].remove(''))
                        for z in range(len(c[i])):
                            c[i][z] = int(c[i][z])
                    a1 = np.array(c)
                    s_expr2 = matrix2.strip(';').split(';')
                    for i in s_expr2:
                        if ' ' in s_expr2:
                            s_expr2.remove(' ')
                    c2 = [i.strip(' ').split(' ') for i in s_expr2]
                    for i in range(len(c2)):
                        for j in range(c2[i].count('')):
                            print(c2[i].remove(''))
                        for z in range(len(c2[i])):
                            c2[i][z] = int(c2[i][z])
                    a2 = np.array(c2)
                    s_expr3 = a1 @ a2
                    #     将矩阵解码为字符串
                    n, m = s_expr3.shape
                    s_expr = s_expr + '\n ' + '乘法结果\n'
                    for i in range(n):
                        for j in range(m):
                            s_expr = s_expr + ' ' + str("%.2f" % s_expr3[i][j])
                            if j == m - 1:
                                s_expr = s_expr + ';\n'
            else:
                s_expr = s_expr + ''
        return s_expr
    except:
        abort(401, msg='输入格式不对')
        return s_expr
