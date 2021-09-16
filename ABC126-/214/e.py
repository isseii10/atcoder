import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def solve():
    n = int(input())
    lr = []
    for _ in range(n):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        lr.append((r, l))
    lr.sort()
    now = -1
    for i in range(n):
        #print(now)
        r, l = lr[i]
        if now+1 < l:
            now = l
        elif l <= now+1 <= r:
            now += 1
        elif r < now+1:
            print("No")
            break
    else:
        print("Yes")

    



def main():
    t = int(input())
    for _ in range(t):
        solve()
if __name__ == '__main__':
    main()