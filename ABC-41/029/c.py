import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    pw = []

    for i in range(3**n):
        tmp = ""
        for _ in range(n):
            if i % 3 == 0:
                tmp += 'a'
            elif i % 3 == 1:
                tmp += 'b'
            else:
                tmp += 'c'
            i //= 3
        pw.append(tmp)
    
    pw.sort()
    for s in pw:
        print(s)

if __name__ == '__main__':
    main()