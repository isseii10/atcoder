import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))
    takahashi_score = 0
    for i in range(n):
        for j in range(n):
            if i == j:continue
            if i < j and (j-i+1) % 2 == 1:
                j -= 1
            elif j < i and (i-j+1) % 2 == 1:
                j += 1
            flag = True
            res = 0
            for k in range(i, j+1):
                if flag:
                    res += a[k]
                flag ^= True
            takahashi_score = max(takahashi_score, res)
    print(takahashi_score)

if __name__ == '__main__':
    main()