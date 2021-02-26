from decimal import *

def delBlank(str):

    ans = ""
    for e in str:
        if e != " ":
            ans += e
    return ans

def precede(a, b):
    # the prior of operator
    prior = (
        #   '+'  '-'  '*'  '/'  '('  ')'  '^'  '#'
           ('>', '>', '<', '<', '<', '>', '<', '>'), # '+'
           ('>', '>', '<', '<', '<', '>', '<', '>'), # '-'
           ('>', '>', '>', '>', '<', '>', '<', '>'), # '*'
           ('>', '>', '>', '>', '<', '>', '<', '>'), # '/'
           ('<', '<', '<', '<', '<', '=', '<', ' '), # '('
           ('>', '>', '>', '>', ' ', '>', '>', '>'), # ')'
           ('>', '>', '>', '>', '<', '>', '>', '>'), # '^'
           ('<', '<', '<', '<', '<', ' ', '<', '=')  # '#'
        )

    # operator to index of prior[8][8]
    char2num = {
        '+': 0,
        '-': 1,
        '*': 2,
        '/': 3,
        '(': 4,
        ')': 5,
        '^': 6,
        '#': 7
        }

    return prior[char2num[a]][char2num[b]]

def operate(a, b, operator):
    """
    Operate [a operator b]
    """
    if operator == '+':
        ans = a + b
    elif operator == '-':
        ans = a - b
    elif operator == '*':
        ans = a * b
    elif operator == '/':
        if b == 0:
            ans = "VALUE ERROR"
        else:
            ans = a / b
    elif operator == '^':
        if a == 0 and b == 0:
            ans = "VALUE ERROR"
        else:
            ans = a ** b

    return ans

def calc(exp):
    exp += '#'
    operSet = "+-*/^()#"
    stackOfOperator, stackOfNum = ['#'], []
    pos, ans, index, length = 0, 0, 0, len(exp)
    while index < length:
        e = exp[index]
        if e in operSet:
            # calc according to the prior
            topOperator = stackOfOperator.pop()
            compare = precede(topOperator, e)
            if compare == '>':
                try:
                    b = stackOfNum.pop()
                    a = stackOfNum.pop()
                except:
                    return "FORMAT ERROR"
                ans = operate(a, b, topOperator)
                if ans == "VALUE ERROR":
                    return ans
                else:
                    stackOfNum.append(ans)
            elif compare == '<':
                stackOfOperator.append(topOperator)
                stackOfOperator.append(e)
                index += 1
            elif compare == '=':
                index += 1
            elif compare == ' ':
                return "FORMAT ERROR"
        else:
            # get the next num
            pos = index
            while not exp[index] in operSet:
                index += 1
            temp = exp[pos:index]

            # delete all 0 of float in the end
            last = index - 1
            if '.' in temp:
                while exp[last] == '0':
                    last -= 1
                temp = exp[pos:last + 1]

            try:
                temp = Decimal(temp)
            except:
                return "INPUT ERROR"
            stackOfNum.append(temp)

    if len(stackOfNum) == 1 and stackOfOperator == []:
        return stackOfNum.pop()
    else:
        return "INPUT ERROR"

def main(stri):
    # get the exp
    exp = stri

    # set the precision
    getcontext().prec = 10

    # delete blanks
    exp = delBlank(exp)

    # calc and print the ans
    ans = calc(exp)
    return ans