#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
INF = float('inf')

def main():
    m = int(input())
    if m < 100:
        print('00')
        exit()
    if m <= 5000:
        sm = str(m)
        if len(sm) == 3:
            ans = "0" + sm[0]
        else:
            ans = sm[:2]
        print(ans)
        exit()
    if m <= 30000:
        km = m //1000
        ans = km+50
        print(ans)
        exit()
    if m <= 70000:
        km = m // 1000
        km -= 30
        km //= 5
        km += 80
        print(km)
        exit()
    
    print(89)


if __name__ == '__main__':
    main()
