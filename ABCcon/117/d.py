import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

"""
ACしたけど調べたら嘘解法だった。。。
5 2
0 0 0 2 2
でX＝1で９が出力されるのが正しい解法
X＝2で6が出力されるのが嘘解法
桁DPを使うのが確実らしい
"""

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    bit = [0]*100
    for a in A:
        loop_count = 0
        _a = a
        while _a > 0:
            if _a % 2:
                bit[loop_count] += 1
            _a //= 2
            loop_count += 1

    #print(bit)
    X = k
    small_flag = False
    for bit_pos in range(len(bit))[::-1]:
        bit_count = bit[bit_pos]
        one = bit_count
        zero = n-bit_count
        if one >= zero:
            #Xのbit_posのビットは０にしたほうが良い
            if X >> bit_pos & 1:
                X &= ~(1<<bit_pos)
                small_flag = True
        else:
            #Xのbit_posのビットは１にした方が良い
            if small_flag:
                X |= (1<<bit_pos)
        #print(X)
    ans = 0
    for a in A:
        ans += X^a
    print(ans)



    

if __name__ == '__main__':
    main()