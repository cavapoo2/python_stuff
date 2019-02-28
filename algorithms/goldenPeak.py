def create_peaks(A):
    N = len(A)
    peaks = [False] * N
    for i in range(1, N - 1):
        if A[i] > max(A[i - 1], A[i + 1]):
            peaks[i] = True
    return peaks

def next_peak(A):
    N = len(A)
    peaks = create_peaks(A)
    next = [0] * N
    next[N - 1] = -1
    for i in range(N - 2, -1, -1):
        if peaks[i]:
            next[i] = i
        else:
            next[i] = next[i + 1]
    return next

def flags(A):
    N = len(A)
    next = next_peak(A)
    i = 1
    result = 0
    while (i - 1) * i <= N:
        pos = 0
        num = 0
        while pos < N and num < i:
            pos = next[pos]
            if pos == -1:
                break
            num += 1
            pos += i
        result = max(result, num)
        i += 1
    return result

d = [1,5 ,3,4,3,4,1,2,3,4,6,2]
print(d)
n = next_peak(d)
print(n)

