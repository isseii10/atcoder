import sys
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def f(x):
    str_x = str(x)
    x_digit = len(str_x)
    c = [0]*10
    for i in range(x_digit):
        c[int(str_x[i])] += 1
    
    g1 = 0
    g2 = 0
    k = x_digit
    for i in range(10)[::-1]:
        if c[i] > 0:
            for _ in range(c[i]):
                g1 += i * 10**(k-1)
                g2 += i * 10**(x_digit-k)
                k -= 1
                #print(g1, g2)
    return  g1 - g2
            
    


def main():
    n, k = map(int, input().split())
    ans = n
    for _ in range(k):
        ans = f(ans)
    print(ans)
if __name__ == '__main__':
    main()