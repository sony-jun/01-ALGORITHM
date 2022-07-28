A, B = map(int, input().split())
number = []

for i in range(1, B):
    for j in range(i):
        number.append(i)

# A부터 B까지 슬라이싱
print(sum(number[A-1:B]))

# 리스트 길이가 1000인 범위 구하기
# number = []

# for i in range(1, 46):
#     for j in range(i):
#         number.append(i)

# print(len(number))