# https://www.acmicpc.net/problem/2592

my_dict = {}
sum_num = 0
for _ in range(10):
    num = int(input())
    sum_num += num
    if num not in my_dict:
        my_dict[num] = 1
    else:
        my_dict[num] += 1
print(int(sum_num / 10))
mode = max(my_dict.values())

for k, v in my_dict.items():
    if v == mode:
        print(k)
        break
