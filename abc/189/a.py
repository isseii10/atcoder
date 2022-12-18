1 #from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
INF = float('inf')

def main():
    s = list(input()[:-1])
    flag = True
    for i in range(2):
        if s[i+1] != s[i]:
            flag = False
    if flag:
        print('Won')
    else:
        print('Lost')
if __name__ == '__main__':
    main()