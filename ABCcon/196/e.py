import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353

def f(t, a, x):
    if t == 1:
        return x+a
    elif t == 2:
        return max(x, a)
    else:
        return min(x, a)

def main():
    n = int(input())
    a = []
    t = []
    for _ in range(n):
        A, T = map(int, input().split())
        a.append(A)
        t.append(T)

    
    q = int(input())
    X = list(map(int, input().split()))
    


if __name__ == '__main__':
    main()