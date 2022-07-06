import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    people_id = []
    for i, num in enumerate(a):
        people_id.append((num, i))
    
    people_id.sort()

    ans = [0]*n

    every = k // n
    k -= every*n

    for i in range(k):
        _, id = people_id[i]
        ans[id] += 1
    
    for i in range(n):
        print(ans[i]+every)
if __name__ == '__main__':
    main()