import sys
from collections import deque, defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    deqs = []
    for _ in range(m):
        k = int(input())
        collors = deque(map(int, input().split()))
        deqs.append(collors)
    #print(deqs)
    
    fronts = defaultdict(list)
    two_collor = deque()
    for i in range(m):
        fronts[deqs[i][-1]].append(i)
        if len(fronts[deqs[i][-1]]) == 2:
            two_collor.append(fronts[deqs[i][-1]])

    for _ in range(n):
        if len(two_collor) == 0:
            print("No")
            exit()
        idx1, idx2 = two_collor.pop()
        fronts[deqs[idx1][-1]] = []
        deqs[idx1].pop()
        deqs[idx2].pop()
        if deqs[idx1]:
            fronts[deqs[idx1][-1]].append(idx1)
            
        if deqs[idx2]:
            fronts[deqs[idx2][-1]].append(idx2)
        if deqs[idx1] and deqs[idx2]:
            if deqs[idx1][-1] == deqs[idx2][-1]:
                two_collor.append(fronts[deqs[idx1][-1]])
            else:
                if len(fronts[deqs[idx1][-1]]) == 2:
                    two_collor.append(fronts[deqs[idx1][-1]])
                if len(fronts[deqs[idx2][-1]]) == 2:
                    two_collor.append(fronts[deqs[idx2][-1]])
        elif deqs[idx1] and not deqs[idx2]:
            if len(fronts[deqs[idx1][-1]]) == 2:
                two_collor.append(fronts[deqs[idx1][-1]])
        elif not deqs[idx1] and deqs[idx2]:
            if len(fronts[deqs[idx2][-1]]) == 2:
                two_collor.append(fronts[deqs[idx2][-1]])
        

    
    print("Yes")


if __name__ == '__main__':
    main()