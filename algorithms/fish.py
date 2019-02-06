def solution(A, B):
    survivals = 0
    stack = []
    for idx in range(len(A)):
        if B[idx] == 0:
            while len(stack) != 0:
                if stack[-1] > A[idx]:
                    break
                else:
                    stack.pop()
            else:
                survivals += 1
        else:
            stack.append(A[idx])
    survivals += len(stack)
    return survivals

A = [ 3,6,9,10,12,2,4,8,7,13,22,5,11];
B = [ 0,1,1,0,0,1,0,1,1,1,1,0,0];
res = solution(A,B)
print(res)
