import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max_a = 10**9
    ans = 0
    used = set()
    for ai in a:
        if ai not in used:
            ans += 1
            used.add(ai)
        while ai <= max_a:
            ai *= 2
            used.add(ai)
    print(ans)

    
if __name__ == '__main__':
    main()