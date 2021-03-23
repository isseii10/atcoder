import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    x = input()[:-1]
    x = list(x.split('.'))
    print(x[0])
    
if __name__ == '__main__':
    main()