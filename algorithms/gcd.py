import sys
def gcd(a, b):
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

def main(argv):
    if(len(argv) > 2):
        r = gcd(int(argv[1]),int(argv[2]))
        print('r=',r)
    else:
        print('must enter 2 integer digits')




if __name__ == "__main__":
    main(sys.argv)



