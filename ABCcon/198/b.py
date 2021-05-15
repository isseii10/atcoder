import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353

def check(s):
    len_s = len(s)
    for i in range(len_s):
        if s[i] != s[len_s-1-i]:
            return False
    return True

def main():
    n = input()[:-1]
    len_n = len(n)
    rev = ""
    first_flag = False
    for i in range(len_n)[::-1]:
        if n[i] == '0' and first_flag == False:
            continue
        first_flag = True
        rev += n[i]
    
    if check(rev):
        print('Yes')
    else:
        print('No')
    



if __name__ == '__main__':
    main()