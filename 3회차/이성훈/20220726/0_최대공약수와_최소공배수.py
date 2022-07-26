# https://www.acmicpc.net/problem/2609
import sys

sys.stdin = open("0_최대공약수와_최소공배수.txt")

A, B = map(int,input().split())

# 최대 공약수 = 공약수 중 가장 큰 수 (max)
for i in range(min(A,B), 0, -1):    # 공약수 중에서 가장 큰 값을 찾아야 하므로 큰 값부터 작은 값으로 내려감
    if A % i == 0 and B % i == 0:   # 공약수 찾는 중
        #print(i)
        gcd = i
        break


# 최소 공배수 = 공배수 중 가장 작은 수 (min)
# for j in range(max(A, B), (A * B) + 1):   # 공배수 중에서 가장 작은 값을 찾아야 하므로 작은 값부터 큰 값으로 올라감
#     if j % A == 0 and j % B == 0:   # 공배수(공약수) 찾는 중
#         print(j)
#         break
print(gcd)
print(A * B // gcd)