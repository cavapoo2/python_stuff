import sys

def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while (i * i <= n):
        if (sieve[i]):
            k = i * i
            while (k <= n):
                sieve[k] = False
                k += i
        i += 1
    return sieve

#smallest prime that devides this number
def arrayF(n):
    F = [0] * (n + 1)
    i = 2
    while (i * i <= n):
        if (F[i] == 0):
            k = i * i
            while (k <= n):
                if (F[k] == 0):
                    F[k] = i;
                k += i
        i += 1
    return F

def factorization(x, F):
    primeFactors = []
    while (F[x] > 0):
        primeFactors += [F[x]]
        x //= F[x]
    primeFactors += [x]
    return primeFactors

def main(argv):
    if(len(argv) > 1):
        A = arrayF(int(argv[1]))
        F = factorization(int(argv[1]),A)
        print(F)


if __name__ == "__main__":
    main(sys.argv)

'''
print('sieve 17')
print(sieve(17))
print('arrayF 17')
print(arrayF(17))
print('primeFactors')
'''

#print(factorization(12,arrayF(12)))
