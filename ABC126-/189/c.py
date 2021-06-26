#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
INF = float('inf')

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    
    for i in range(n):
        min_a = a[i]
        for j in range(i, n):
            min_a = min(min_a, a[j])
            ans = max(ans, min_a*(j-i+1))


    print(ans)



if __name__ == '__main__':
    main()