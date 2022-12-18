import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    vote = defaultdict(int)
    for _ in range(n):
        s = input()[:-1]
        vote[s] += 1
    
    leader = ""
    max_vote = 0
    for name, num in vote.items():
        if max_vote < num:
            max_vote = num
            leader = name
    print(leader)

if __name__ == '__main__':
    main()