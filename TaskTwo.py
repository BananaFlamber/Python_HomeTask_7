import random
import string
import numpy as np
def RndExpr():
    N = random.randrange(2,11)
    lst_digit = list(np.random.choice(list(string.digits), N))
    lst_oper = list(np.random.choice(['+','-'], N-1))
    result = [None]*(2*N - 1)
    result[::2] = lst_digit
    result[1::2] = lst_oper
    return "".join(result)
for i in range(0,5):
    s = RndExpr()
    print()
    print(s, "=" ,eval(s))
    oper = s[1::2]
    j = 0
    result = int(s[0])
    for x in oper:
        digit = int(s[2*j+2])
        if x == '+':
            result += digit
        else:
            result -= digit
        j += 1
    print(s, "=" ,result)