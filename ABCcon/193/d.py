import sys
from collections import Counter

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    k = int(input())
    s = input()[:-1]
    t = input()[:-1]
    s_count = [0]*10 #takahashi
    t_count = [0]*10 #aoki
    for i in range(4):
        s_count[ord(s[i])-ord('0')] += 1
        t_count[ord(t[i])-ord('0')] += 1
    #print(s_count)
    #print(t_count)
    nokori = [k]*10
    for i in range(1, 10):
        nokori[i] -= (s_count[i]+t_count[i])
    

    total = sum(nokori) - k
    ans = 0
    for i in range(1, 10):
        if nokori[i] == 0:continue
        takahashi = [0]*10
        takahashi[i] = 1

        takahashi_score = 0
        for j in range(1, 10):
            takahashi_score += j * 10 **(s_count[j]+takahashi[j])
        takahashi_i = nokori[i]
        
        for a in range(1, 10):
            if nokori[a] - takahashi[a] == 0:continue
            aoki = [0]*10
            aoki[a] = 1
            aoki_a = (nokori[a] - takahashi[a])

            aoki_score = 0
            for b in range(1, 10):
                aoki_score += b * 10 ** (t_count[b]+aoki[b])
            
            if takahashi_score > aoki_score:
                ans += takahashi_i * aoki_a / (total*(total-1))
        
    print("{:.10f}".format(ans))

            


if __name__ == '__main__':
    main()