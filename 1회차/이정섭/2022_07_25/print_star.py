# Baekjoon_2438

# 별 찍기 - 1

# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

stars=int(input())

for star in range(1,stars+1):
    print("*"*star)