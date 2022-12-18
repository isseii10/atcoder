import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    sum_a = sum(a)
    count = 0
    if x > sum_a:
        count = x // sum_a
        x %= sum_a
    res = 0
    for i in range(n):
        res += a[i]
        if res > x:
            k = i+1
            break
    

    print(n*count + k) 

if __name__ == '__main__':
    main()