import inspect
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    can_use_num = [0]*n
    for i in range(n):
        can_use_num[i] = a[i] // x
    if sum(can_use_num) < k:
        leave = k-sum(can_use_num)
        pay = []
        for i in range(n):
            pay.append(a[i]%x)
        pay.sort(reverse=True)
        print(sum(pay[leave:]))
    else:
        print(sum(a)-k*x)
if __name__ == '__main__':
    main()