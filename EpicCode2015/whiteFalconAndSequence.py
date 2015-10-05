N = int(raw_input())
A = map(int, raw_input().split(" "))

def addUpFunc(x, y):
    retval = 0
    y = y[::-1]
    for i in range(len(x)):
        retval += (x[i]*y[i])
    return retval
