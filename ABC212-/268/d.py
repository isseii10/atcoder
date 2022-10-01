import sys
from itertools import permutations
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def trim(t):
    newT = set()
    for moji in t:
        mojis = moji.split("_")
        newMoji = ""
        for c in mojis:
            if c[0] == "" or c[-1] == "":
                continue
            newMoji += c
        newT.add(newMoji)
    return newT

def main():
    n, m = map(int, input().split())
    s = []
    lenRawS = 0
    for _ in range(n):
        kouho = input()[:-1]
        lenRawS += len(kouho)
        s.append(kouho)
    out = set()
    for _ in range(m):
        out.add(input()[:-1])
    permS = permutations(s)
    for p in permS:
        nokori = 16 - lenRawS
        if nokori == n-1:
            a = "_".join(p)
            if a  not in out:
                print(a)
                exit()
        else:
            nokori -= n-1
            a = ""
            for i, s in enumerate(p):
                for j in range(nokori):
                    









    
if __name__ == '__main__':
    main()