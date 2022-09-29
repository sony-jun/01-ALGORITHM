# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

A,B =(input().split())

A = int(A)
B = int(B)

from math import gcd

GCD = gcd(A,B)
LCM = A * B // GCD

print(GCD)
print(LCM)
