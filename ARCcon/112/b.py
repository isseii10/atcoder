import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    B, C = map(int, input().split())
    # B = 0の時に注意
    if B<=C:
        if B > 0:
            ans = B*2+C -1
        else:
            ans = abs(B)*2 + C
    else:
        ans = C + 1

    print(ans)
    

    
if __name__ == '__main__':
    main()