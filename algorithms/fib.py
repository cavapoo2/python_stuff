import numpy as np

def fib1(n):
    m = np.array([[1,1],[1,0]])
    r = np.linalg.matrix_power(m,n);
    return r[0][1]

def fib2(n):
    if n < 1:
        return 0
    if(n < 2):
        return 1;
    a2=0
    a1=1
    for _ in range(0,n-1):
        r = a1 + a2
        a2=a1
        a1=r
    return r


