import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    x = input()[:-1]
    ch_flag = False
    for i, c in enumerate(x):
        if ch_flag:
            ch_flag = False
            continue
        if c in {'o', 'k', 'u'}:
            continue
        if c == 'c':
            if i < len(x)-1 and x[i+1] == 'h':
                ch_flag = True
                continue
        
        break

    else:
        print("YES")
        exit()

    print('NO')
    
if __name__ == '__main__':
    main()