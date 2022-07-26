import sys
from math import gcd

input = sys.stdin.readline

n, m = map(int, input().split())
number_gcd = gcd(n, m)

print(number_gcd)
print(number_gcd * (n // number_gcd) * (m // number_gcd))