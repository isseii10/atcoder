import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    n = len(s)
    k = int(input())
    used = set()
    for i in range(n-k+1):
        used.add(s[i:i+k])
    print(len(used))
if __name__ == '__main__':
    main()