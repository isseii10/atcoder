import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def main():
    s = input()[:-1]
    n = len(s)
    len_count = 1 # s[0]の分
    bit_length = []
    for i in range(1, n):
        if s[i] == s[i-1]:
            len_count += 1
        else:
            bit_length.append((int(s[i-1]), len_count))
            len_count = 1

        if i == n-1:
            bit_length.append((int(s[i]), len_count))
    #print(bit_length)
    m = len(bit_length)
    acc = [0]*(m+1)
    for i in range(m):
        acc[i+1] = acc[i] + bit_length[i][1]
    ans = n
    for i in range(m-1):
        ans = min(ans, max(acc[i+1], n-acc[i+1]))
    print(ans)


if __name__ == '__main__':
    main()