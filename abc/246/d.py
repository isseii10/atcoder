import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    # (a+b)**3 = a**3 + 3a**2 b + 3a b**2 +b**3
    # X = (a+b)**3 - 2ab(a+b)
    # X = (a+b){(a+b)**2 - 2ab}
    # X = (a+b)(a**2 + b**2)
    
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
    divs = divisor(n)
    divs.sort()
    
if __name__ == '__main__':
    main()