import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    o_list = []
    x_list = []
    for i in range(10):
        if s[i] == 'o':
            o_list.append(str(i))
        elif s[i] == 'x':
            x_list.append(str(i))
    
    n = len(o_list)
    m = len(x_list)
    
    ans = 0
    for i in range(10000):
        i = str(i)
        while len(i) < 4:
            i = '0' + i
        #print(i)
        i_list = list(i)
        #print(i_list)
        o_is_ok = False
        x_is_ok = False
        for o in o_list:
            if o not in i_list:
                break
        else:
            o_is_ok = True

        for num in i_list:
            if num in x_list:
                break
        else:
            x_is_ok = True
        
        if o_is_ok and x_is_ok:
            ans += 1
    print(ans)
    
    

if __name__ == '__main__':
    main()