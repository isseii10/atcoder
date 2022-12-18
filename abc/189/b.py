#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
INF = float('inf')

def main():
    n, x = map(int, input().split())
    vp = [list(map(int, input().split())) for _ in range(n)]
    #print(vp)
    now = 0
    ans = -1
    x *= 100
    for i in range(n):
        v, p = vp[i]
        now += v * p
        if now > x:
            ans = i+1
            break
    print(ans)
if __name__ == '__main__':
    main()