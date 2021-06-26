import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for idx, num in enumerate(a):
        #print(num, idx)
        if num != idx+1:
            break
    else:
        print("Yes")
        exit()
    print("No")
if __name__ == '__main__':
    main()