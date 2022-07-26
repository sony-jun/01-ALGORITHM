a,b = (input().split())
a = int(a)
b = int(b)

from math import gcd


GCD = gcd(a, b)
LCM = a * b // GCD

print(GCD)
print(LCM)


# Wrong
# from math import gcd

# a, b = int(input().split())
# cd = int(gcd(a, b))
# cm = int(a * b // cd)

# print(int(cd))
# print(int(cm))

# Reason
# line - a, b = int(input().split())
# TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
# using split method turns into list.
# The split() method splits a string into a list. You can specify the separator, default separator is any whitespace.
