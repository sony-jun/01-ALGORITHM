import sys

sys.stdin = open("0_최대공약수최소공배수.txt")



n, m = map(int, input().split())

n_factors = [] # n 의 인수들 # 24
m_factors = [] # m 의 인수들 # 18

for i in range(1, n + 1):
    if n % i == 0:
        n_factors.append(i) # 나누어 떨어지는 것만 추가

for j in range(1, m + 1):
    if m % j == 0:
        m_factors.append(j) # 나누어 떨어지는 것만 추가

factors = n_factors + m_factors # 인수들의 합집합

factors = list(set(factors)) # 겹치는 숫자 없애기

common_factor = [] # 공약수들의 집합

for k in factors:
    if n % k == 0 and m % k == 0:
        common_factor.append(k) # 공약수들만 추가

n_maxfactor = n // max(common_factor)
m_maxfactor = m // max(common_factor)

least_multiple = n_maxfactor * m_maxfactor * max(common_factor)

print(max(common_factor))
print(least_multiple)



'''
n, m = map(int, input().split())

n_factors = []
m_factors = []

for i in range(1, n + 1):
    if n % i == 0:
        n_factors.append(i)

for j in range(1, m + 1):
    if m % j == 0:
        m_factors.append(j)

factors = n_factors + m_factors

factors = list(set(factors))
res = []

for k in factors:
    if n % k == 0 and m % k == 0:
        res.append(k)

small = 0
big = 0
if n > m:
    big = n
    small = m
else:
    big = m
    small = n

s = small
b = big
while 1:
    small += s
    if small > big:
        big += b
    if small == big:
        break
    
print(max(res))
print(small)
'''