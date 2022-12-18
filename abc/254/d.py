import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

# nの素因数分解(O(n**0.5)
def prime_factor(n):
    ass = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass

def main():
    n = int(input())
    count = [0] * (n+1)
    for i in range(1, n+1):
        m = i
        d = 2
        while d*d <= i:
            while m % (d**2) == 0:
                m //= d**2
            d += 1
        count[m] += 1
    ans = 0
    for c in count:
        ans += c*c
    print(ans)
        

        
if __name__ == '__main__':
    main()