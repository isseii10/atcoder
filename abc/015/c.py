import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    prev_set = set(t[0])
    for i in range(1, n):
        now_set = set()
        for x in t[i]:
            for prev_num in prev_set:
                res = x^prev_num
                now_set.add(res)
        prev_set = now_set

    if 0 in prev_set:
        print("Found")
    else:
        print("Nothing")    

if __name__ == '__main__':
    main()