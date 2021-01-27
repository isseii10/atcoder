x, y = map(int ,input().split())
group1 = set([1, 3, 5, 7, 8, 10, 12])
group2 = set([4, 6, 9, 11])
if x in group1 and y in group1:
    print("Yes")
    exit()
if x in group2 and y in group2:
    print("Yes")
    exit()
print("No") 