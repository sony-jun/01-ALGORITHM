# https://www.acmicpc.net/problem/2587

input_list = []

for _ in range(5):
    input_list.append(int(input()))
print(int(sum(input_list) / 5))

input_list = sorted(input_list)
print(input_list[2])