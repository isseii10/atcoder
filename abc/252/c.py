import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    ss = [input()[:-1] for _ in range(n)]
    ans = INF
    for target in range(10):
        count = [0]*10 # count[t] := t秒時にtargetが表示されている個数
        for time in range(10):
            for s in ss:
                if s[time] == "{}".format(target):
                    count[time] += 1
        res = 0
        max_count = max(count)
        for t in range(10)[::-1]:
            if count[t] == max_count:
                res += t
                res += (count[t]-1)*10
                break
        #print("target: {}, time: {}".format(target, res))
        ans = min(ans, res)
    print(ans)

            

            
if __name__ == '__main__':
    main()