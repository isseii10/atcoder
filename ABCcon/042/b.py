#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
INF = float('inf')

def main():
    n, l = map(int, input().split())
    s_list = [input()[:-1] for _ in range(n)]
    s_list.sort()
    print(''.join(s_list))
if __name__ == '__main__':
    main()