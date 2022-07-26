num1, num2 = map(int, input().split())

#최대공약수
for i in range(min(num1, num2), 0, -1):
    if num1%i==0 and num2%i==0:
        print(i)
        break
#최소공배수
for j in range(max(num1, num2), (num1*num2)+1):
    if j%num1==0 and j%num2==0:
        print(j)
        break
# 시간 초과=====================================

import math
#최대공약수
print(math.gcd(num1, num2))
#최소공배수
print(math.lcm(num1, num2))