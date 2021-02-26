from flask_restful import abort
import numpy as np

def Matrix_operation(matrix1,determinant,transpose,trace,rank,inverse,eigenvalues,triangularly,square):
    s_expr = ''
    try:
        if matrix1 != '':
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
                print(a1)
                if determinant == 'on':
                    det = np.linalg.det(a1)
                    s_expr = '行列式\n' + str(det) + '\n'
                else:
                    s_expr = ''
                if transpose == 'on':
                    a11 = np.transpose(a1)
                    n, m = a11.shape
                    s_expr = s_expr + '\n ' + '矩阵转置\n'
                    for i in range(n):
                        for j in range(m):
                            s_expr = s_expr + ' ' + str("%.2f" % a11[i][j])
                            if j == m - 1:
                                s_expr = s_expr + ';\n'
                else:
                    s_expr = s_expr + ''
                if trace == 'on':
                    a12 = np.linalg.inv(a1)
                    print(a12)
                    n, m = a12.shape
                    s_expr = s_expr + '\n ' + '矩阵的逆\n'
                    for i in range(n):
                        for j in range(m):
                            s_expr = s_expr + ' ' + str("%.2f" % a12[i][j])
                            if j == m - 1:
                                s_expr = s_expr + ';\n'
                else:
                    s_expr = s_expr + ''
                if rank == 'on':
                    rank = np.linalg.matrix_rank(a1)
                    s_expr = s_expr + '秩\n' + str(rank) + '\n'
                else:
                    s_expr = s_expr + ''
                if inverse == 'on':
                    tr = np.trace(a1)
                    s_expr = s_expr + '迹\n' + str(tr) + '\n'
                else:
                    s_expr = s_expr + ''
                if eigenvalues == 'on':
                    x, y = np.linalg.eig(a1)
                    s_expr = s_expr + '特征值\n' + str(x)
                    n, m = y.shape
                    s_expr = s_expr + '\n ' + '特征向量\n'
                    for i in range(n):
                        for j in range(m):
                            s_expr = s_expr + ' ' + str("%.2f" % y[i][j])
                            if j == m - 1:
                                s_expr = s_expr + ';\n'
                else:
                    s_expr = s_expr + ''
                if triangularly == 'on':
                    arr = np.triu(a1, 0)
                    arr2 = np.tril(a1, 0)
                    n, m = arr.shape
                    s_expr = s_expr + '\n ' + '矩阵的上三角部分\n'
                    for i in range(n):
                        for j in range(m):
                            s_expr = s_expr + ' ' + str("%.2f" % arr[i][j])
                            if j == m - 1:
                                s_expr = s_expr + ';\n'
                    n, m = arr2.shape
                    s_expr = s_expr + '矩阵的下三角部分\n'
                    for i in range(n):
                        for j in range(m):
                            s_expr = s_expr + ' ' + str("%.2f" % arr2[i][j])
                            if j == m - 1:
                                s_expr = s_expr + ';\n'
                    else:
                        s_expr = s_expr + ''
                if square == 'on':
                    s_expr3 = a1 @ a1
                    #     将矩阵解码为字符串
                    n, m = s_expr3.shape
                    s_expr = s_expr + '\n ' + '矩阵平方\n'
                    for i in range(n):
                        for j in range(m):
                            s_expr = s_expr + ' ' + str("%.2f" % s_expr3[i][j])
                            if j == m - 1:
                                s_expr = s_expr + ';\n'
        return  s_expr
    except:
        abort(401, msg='输入格式不对')
        return s_expr