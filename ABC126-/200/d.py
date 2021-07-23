import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_idx = [[num%200, i] for i, num in enumerate(a)]
    a_idx.sort()

    mod_a = []
    for i in range(n):
        mod_a.append(a[i]%200)
    
    #modに被りがある時
    kaburi = []
    for i in range(n):
        if mod_a.count(mod_a[i]) > 1:
            kaburi.append(i)
    if len(kaburi) > 1:
        print('Yes')
        print(1, kaburi[0] + 1)
        print(1, kaburi[1] + 1)
        exit()
    #modに被りなし
        


    

    

    

    

if __name__ == '__main__':
    main()