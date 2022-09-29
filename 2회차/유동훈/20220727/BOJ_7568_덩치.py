# https://www.acmicpc.net/problem/7568
# 덩치

# 풀이
N = int(input())
height_list = []
weight_list = []
grade = [1] * N

for i in range(N):
    height, weight = map(int, input().split())
    height_list.append(height)
    weight_list.append(weight)

for j in range(N):
    for k in range(N):
        if height_list[j] < height_list[k] and weight_list[j] < weight_list[k]:
            grade[j] += 1

grade = ' '.join(str(l) for l in grade)
print(grade)