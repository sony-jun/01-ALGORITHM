# https://www.acmicpc.net/problem/2609
A, B = map(int, input().split())
a, b = A, B

while b != 0: # 
    a = a % b
    a, b = b, a
print(a) # 최대공약수
print(A*B//a) # 최소공배수 





# for i in range(min(A, B), 0, -1):
#     if A % i == 0 and B % i == 0:
#         print(i)
#         break

# for j in range(max(A, B), (A * B) + 1):
#     if j % A == 0 and j % B == 0:
#         print(j)
#         break

# for j in range(1, B + 1):
#     if B % j == 0:
#         measure_B.append(j)
# # print(measure_B)

# for i in measure_B:
#     for j in measure_A: 
#         if i == j:
#             measure.append(i)
# print(max(measure))