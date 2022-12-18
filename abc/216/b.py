import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    name = []
    for _ in range(n):
        s, t = input().split()
        name.append([s, t])
    for i in range(n):
        for j in range(n):
            if i == j:continue
            if name[i][0] == name[j][0] and name[i][1] == name[j][1]:
                print("Yes")
                exit()
    
    
    print("No")

if __name__ == '__main__':
    main()