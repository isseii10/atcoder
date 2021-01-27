#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
INF = float('inf')

def main():
    n = int(input())
    s = [int(input()) for _ in range(n)]
    s.sort()
    ans = sum(s)
    if ans % 10 != 0:
        print(ans)
        exit()
    flag = False
    for i in range(n):
        if s[i] % 10 != 0:
            ans -= s[i]
            flag = True
            break
    if not flag:
        ans = 0
    print(ans)

if __name__ == '__main__':
    main()