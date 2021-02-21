import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353

def conv(X : str, n : int) -> int:
    ret = 0
    for i in range(len(X)):
        digit = len(X) - i-1
        ret += int(X[i]) * n**digit
    return ret


def main():
    x = input()[:-1]
    m = int(input())
    #------------------------
    #xの長さが１の時に気づけなかった
    if len(x) == 1:
        if int(x) <= m:
            print(1)
        else:print(0)
        exit()
    #------------------------
    
    d = 0
    for c in x:
        d = max(int(c), d)
    ok = d
    ng = d + 10**100
    while ng - ok > 1:
        mid = (ok + ng) // 2
        #print(conv(x, mid), mid)
        if conv(x, mid) <= m:
            ok = mid
        else:
            ng = mid
    print(ok-d)
        
    

    
if __name__ == '__main__':
    main()