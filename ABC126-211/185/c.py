import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

l = int(input())
l -= 12
ans = combinations_count(l+11, 11)
print(ans)