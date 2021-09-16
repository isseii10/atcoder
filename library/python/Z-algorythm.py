#sとs[i:]の接頭辞が何文字同じになるか
def z_algorythm(s):
    n = len(s)
    LCP = [0]*n
    c = 0
    for i in range(1, n):
        if i + LCP[i-c] < c + LCP[c]:
            LCP[i] = LCP[i-c]
        else:
            j = max(0, c+LCP[c]-i)
            while i+j < n and s[j] == s[i+j]:
                j += 1
            c = i
            LCP[i] = j
    LCP[0] = n
    return LCP

print(z_algorythm(input()))