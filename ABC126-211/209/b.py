import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    price = 0
    for i in range(n):
        price += a[i]
        if (i + 1)%2 == 0:
            price -= 1
    
    if x >= price:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()