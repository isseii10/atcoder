import sys
from itertools import permutations

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def s_to_num(s, d):
    ret = 0
    for c in s:
        ret = ret*10 + d[c]
    ret_str = str(ret)
    ret_len = len(ret_str)
    if len(s) != ret_len or ret == 0:
        return -1
    else:
        return ret


def main():
    s1 = input()[:-1]
    s2 = input()[:-1]
    s3 = input()[:-1]

    alpha = set(s1+s2+s3)
    
    num = len(alpha)
    alpha = list(alpha)
    
    if num > 10:
        print("UNSOLVABLE")
        exit()



    for p_list in permutations(range(10), num):
        d = dict()
        for num, s in zip(p_list, alpha):
            d[s] = num
        n1 = s_to_num(s1, d)
        n2 = s_to_num(s2, d)
        n3 = s_to_num(s3, d)
        if n1 == -1 or n2 == -1 or n3 == -1:continue
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            exit()
    
    print("UNSOLVABLE")



if __name__ == '__main__':
    main()