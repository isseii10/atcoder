import sys
from itertools import combinations, combinations_with_replacement, permutations, product

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s, k = input().split()
    k = int(k)

    list_all = set(permutations(s))
    list_all = list(list_all)
    list_all.sort()
    #print(list_all)
    print("".join(list_all[k-1]))

if __name__ == '__main__':
    main()