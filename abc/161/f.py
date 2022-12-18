import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def fctr1(n):
    f = []
    c = 0
    r = int(n**0.5)
    for i in range(2, r+2):
        while n % i == 0:
            c += 1
            n = n//i
        if c != 0:
            f.append([i, c])
            c = 0
    if n != 1:
        f.append([n, 1])
    return f

def extGCD(a, b):
    if a==0: return (0, 1, b)

    (X, Y, g) = extGCD(b%a, a)
    return (Y-b//a*X, X, g)


def GCD(a, b):
    if a==0:
        return b
    return GCD(b%a, a)

def main():
    n = int(input())
    print(fctr1(n))
    for i in range(2, n+1):
        print("=====================")
        if n % i != 0:
            print(n%i)
        else:
            n_ = n
            while n_%i==0:
                n_ //= i
            print(n_)
        print("=====================")
        

    
if __name__ == '__main__':
    main()