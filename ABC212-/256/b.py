import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    As = list(map(int, input().split()))
    p = 0
    field = [0]*4
    for a in As:
        field[0] += 1
        for i in range(4)[::-1]:
            if i+a > 3:
                p += field[i]
                field[i] = 0
            else:
                field[i+a] = field[i]
                field[i] = 0
                
    print(p)
        
if __name__ == '__main__':
    main()