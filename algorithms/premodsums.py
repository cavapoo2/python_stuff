#not sure this is 100% accurate even though it scored 100% on codility
def preModSums(A,B,K):
    if A == B: return 1 if A % K == 0 else 0
    if B < K: return 0
    while (A % K != 0) and (A < B) :
        A+=1

    diff = B - A
    r = diff // K
    return r+1 

def preModSumsSlow(A,B,K):
    sum = 0
    for v in range(A,B+1):
        if (v % K) == 0:
            sum+=1
    return sum


s = preModSumsSlow(0,2,2)
f = preModSums(0,2,2)
print('res=',s,f)
s = preModSumsSlow(11,345,17)
f = preModSums(11,345,17)
print('res=',s,f)
s = preModSumsSlow(6,11,2)
f = preModSums(6,11,2)
print('res=',s,f)
