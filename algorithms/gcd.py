import sys
def gcd(a, b):
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

def gcd2(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def gcd3(a, b, res):
    if a == b:
        return res * a
    elif (a % 2 == 0) and (b % 2 == 0):
        return gcd3(a // 2, b // 2, 2 * res)
    elif (a % 2 == 0):
        return gcd3(a // 2, b, res)
    elif (b % 2 == 0):
        return gcd3(a, b // 2, res)
    elif a > b:
        return gcd3(a - b, b, res)
    else:
        return gcd3(a, b - a, res)

def lcm(a,b):
    return a*b // gcd3(a,b,1)

def main(argv):
    if(len(argv) > 2):
        a= int(argv[1])
        b= int(argv[2])
        r = gcd(a,b)
        print('r=',r)
        r2 = gcd2(a,b)
        print('r2=',r2)
        r3 = gcd3(a,b,1)
        print('r3=',r3)
        r4 = lcm(a,b)
        print('lcm=',r4)

    else:
        print('must enter 2 integer digits')


if __name__ == "__main__":
    main(sys.argv)



