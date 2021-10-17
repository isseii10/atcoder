import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    t = input()[:-1]
    
    idxs = []
    for i in range(len(s)):
        if s[i] != t[i]:
            idxs.append(i)

    ok = False
    if len(idxs) == 0:
        ok = True
    elif len(idxs) == 2:
        first = idxs[0]
        second = idxs[1]
        if first > second:
            first, second = second, first
        if first+1 == second:
            if s[first] == t[second] and s[second] == t[first]:
                ok = True
    
    if ok:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()