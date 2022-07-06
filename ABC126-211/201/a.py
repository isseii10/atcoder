import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    As = list(map(int, input().split()))
    As.sort()
    if As[2] - As[1] == As[1] - As[0]:
        print("Yes")
    else:
        print("No")

    
if __name__ == '__main__':
    main()