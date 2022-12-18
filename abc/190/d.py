import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

#nの約数列挙
def divisor(n):
    ass = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass  # sortされていない

def main():
    n = int(input())
    ans = 0
    for k in range(1, int(n**(0.5))*2):
        uhen = -k**2 + k +2*n
        if uhen > 0 and uhen % (2*k) == 0:
            ans += 2
    print(ans)

if __name__ == '__main__':
    main()