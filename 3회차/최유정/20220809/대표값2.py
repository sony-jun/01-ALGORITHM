# https://www.acmicpc.net/problem/2587
num_list = []
for i in range(5):
    num = int(input())
    num_list.append(num)
num_avg = sum(num_list) // 5
num_list.sort()
center = num_list[2]
print(num_avg)
print(center)
