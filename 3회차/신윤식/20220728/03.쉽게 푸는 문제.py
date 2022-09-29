# https://www.acmicpc.net/problem/1292

A, B = map(int,input().split())
lst = []
count = 1 # 반복할 횟수

for i in range(1,B+1): # i는 반복할 숫자
    for j in range(count): # count번 반복하여 리스트에 숫자 넣어줌
        lst.append(i)
    count+=1 # 반복할 횟수 하나증가

print(sum(lst[A-1:B])) # [1, 2, 2, 3, 3, 3, ...] 식으로 들어갔으므로 인덱스값은 -1을 해줘야함

# 괜찮아보이는 풀이
# suyeol = []

# for i in range(1, 1001):
#     suyeol.extend([i] * i)

# a, b = map(int, input().split())
# sum = 0

# for i in range(a-1, b):
#     sum += suyeol[i]
    
# print(sum)