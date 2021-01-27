def GCD(a, b):
    if a==0:
        return b
    return GCD(b%a, a)


'''
a*x + b*y = gcd(a, b)
gcdの再帰から、(b%a)*X + a*Y = gcd(a, b)が導かれる.
b%a + b//a*a = bより、
b%a*X = b*X - b//a*a*X
(b*X - b//a*a*X) + a*Y = gcd(a,b)
a*(Y - b//a*X) + b*X = gcd(a,b)
'''
# return (x, y, gcd(a,b)) 
# ax + by = gcd(a,b)を満たす整数x,yが求まる
def extGCD(a, b):
    if a==0: return (0, 1, b)

    (X, Y, g) = extGCD(b%a, a)
    return (Y-b//a*X, X, g)

print(extGCD(111, 30))