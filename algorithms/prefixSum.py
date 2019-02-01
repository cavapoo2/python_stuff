def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P
def prefix_diffs(A):
    n = len(A)
    P=[0]* (n+1)
    for k in range(1,n+1):
        P[k] = P[k-1] - A[k-1]
    return P

def avgN(A,N): 
    P= [0]* (len(A)+1)
    for i in range(0, len(A)-N+1):
        avg=0.0
        for j in range(i,i+N):
            avg += A[j]
        P[i] = avg / N
    return P

    
 
ina = [50,1,99,6,7,60,33,-30,10,7,99,1,2,3,50]
ina2 = [-3, -5, -8, -4, -10];
print(ina)
print('pre')
res = prefix_sums(ina)
print(res)
res = prefix_sums(ina2)
print(res)


#print('diffs')
#d = prefix_diffs(ina)
print('avgs')
a = avgN(ina,2)
print(a)
print('avg2')
a2 = avgN(ina2,2)
a3 = avgN(ina2,3)
print(ina2)
print(a2)
print(a3)

