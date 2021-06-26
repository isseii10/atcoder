from bisect import bisect_right

a = [1, 2, 3, 3, 4, 5, 5]
i = bisect_right(a, 3)
print(i)