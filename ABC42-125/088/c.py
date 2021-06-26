grid = [list(map(int, input().split())) for _ in range(3)]

sa = [[0]*2 for _ in range(3)]
flag = True
for i in range(3):
    for j in range(2):
        sa[i][j] = grid[i][j+1] - grid[i][j]
        if i>0:
            if sa[i][j] != sa[i-1][j]:
                flag = False
                break
    if not flag:
        break
                
#print(sa)
if flag:
    print("Yes")
else:
    print("No")