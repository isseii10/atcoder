import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
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

def main():
    k = int(input())
    ans = 0
    for abc in range(1, k+1):
        primes = fctr1(abc)
        res = 1
        for prime, num in primes:
            res *= (num+2)*(num+1)//2
        ans += res
    print(ans)

        

if __name__ == '__main__':
    main()