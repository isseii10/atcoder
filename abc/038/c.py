import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))
    len_list = []
    len = 1
    for i in range(1, n):
        if a[i-1] < a[i]:
            len += 1
        else:
            len_list.append(len)
            len = 1
    len_list.append(len)
    #print(len_list)
    ans = 0
    for l in len_list:
        ans += (1 + l)*l // 2
    print(ans)

            
if __name__ == '__main__':
    main()