import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    As = [] 
    
    for _ in range(n):
        la = list(map(int, input().split()))
        _, a = la[0], la[1:]
        As.append(tuple(a))
        
    #print(As)
    #print(set(As))
    ans = len(set(As))
    print(ans)
if __name__ == '__main__':
    main()