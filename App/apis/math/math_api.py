from flask_restful import Resource,reqparse, abort
from App.apis.api_constant import DER, ININ, DEFI, LIMIT, FRA, MATX, MATOP, FAC, EQA
from App.apis.math.Indefinite_integral import Indefinite_integralIndefinite_integral
from App.apis.math.definite_integral import Definite_integral
from App.apis.math.derivatives import Derivatives
from App.apis.math.equations_set import Equations_set
from App.apis.math.factorial import Factorial
from App.apis.math.fraction import Fraction
from App.apis.math.limit import Limit
from App.apis.math.matrix import Matrix
from App.apis.math.matrix_operation import Matrix_operation

global send_mail_code
parser_math = reqparse.RequestParser()
parser_math.add_argument('title', type=str, required=True,help='未输入计算类型')
parser_math.add_argument('function', type=str, required=True,help='未输入函数表达式')
parser_math.add_argument('var')
parser_math.add_argument('order')
parser_math.add_argument('limit_type')
parser_math.add_argument('a')
parser_math.add_argument('b')
parser_math.add_argument('val')
parser_math.add_argument('matrix1')
parser_math.add_argument('matrix2')
parser_math.add_argument('add')
parser_math.add_argument('sub')
parser_math.add_argument('multi')
parser_math.add_argument('determinant')
parser_math.add_argument('transpose')
parser_math.add_argument('trace')
parser_math.add_argument('rank')
parser_math.add_argument('inverse')
parser_math.add_argument('triangularly')
parser_math.add_argument('eigenvalues')
parser_math.add_argument('square')
parser_math.add_argument('number')
parser_math.add_argument('eigenvalues')

class MathResource(Resource):
    @property
    def post(self):
        s_expr=''
        args = parser_math.parse_args()
        title = args.get('title')
        
        function = args.get('function')
        if title==DER:
            var_s = args.get('var')
            order = args.grt('order')
            s_expr=Derivatives(function,order,var_s)
            data = {'msg': '导数',
                    'status': 201,
                    'data':s_expr}
            return data
        elif title==ININ:
            var_s = args.get('var')
            s_expr=Indefinite_integralIndefinite_integral(function,var_s)
            data = {'msg': '不定积分',
                    'status': 201,
                    'data': s_expr}
            return data
        elif title == DEFI:
            var_s = args.get('var')
            a=args.get('a')
            b=args.get('b')
            s_expr=Definite_integral(function, var_s,a,b)
            data = {'msg': '定积分',
                    'status': 201,
                    'data': s_expr}
            return data
        elif title == LIMIT:
            var_s = args.get('var')
            limit_type=args.get('limit_type')
            val=args.get('val')
            s_expr=Limit(function, var_s, limit_type, val)
            data = {'msg': '极限',
                    'status': 201,
                    'data': s_expr}
            return data
        elif title == FRA:
            s_expr=Fraction(function)
            data = {'msg': '分数',
                    'status': 201,
                    'data': s_expr}
            return data
        elif title == MATX:
            matrix1=args.get('matrix1')
            matrix2=args.get('matrix2')
            add=args.get('add')
            sub=args.get('sub')
            multi=args.get('multi')
            s_expr=Matrix(matrix1, matrix2, add, sub, multi)
            data = {'msg': '方程组',
                    'status': 201,
                    'data': s_expr}
            return data
        elif title == MATOP:
            matrix1 = args.get('matrix1')
            determinant=args.get('determinant')
            transpose=args.get('transpose')
            trace=args.get('trace')
            rank=args.get('rank')
            inverse=args.get('inverse')
            triangularly=args.get('triangularly')
            eigenvalues=args.get('eigenvalues')
            square=args.get('square')
            s_expr=Matrix_operation(matrix1,determinant,transpose,trace,rank,inverse,eigenvalues,triangularly,square)
            data = {'msg': '矩阵基本运算',
                    'status': 201,
                    'data': s_expr}
            return data
        elif title == FAC:
            number=args.get('number')
            s_expr=Factorial(number)
            data = {'msg': '矩阵高级运算',
                    'status': 201,
                    'data': s_expr}
            return data
        elif title == EQA:
            s_expr=Equations_set(function)
            data = {'msg': '阶乘',
                    'status': 201,
                    'data': s_expr}
            return data
