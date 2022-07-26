a, b = map(int, input().split())
c, d = a, b
while d != 0:
    c = c%d
    c, d = d, c
e = a*b//c

print(c)
print(e)







# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# print(gcd(a, b), a*b//gcd(a, b))
