# https://www.acmicpc.net/problem/1371

import sys

input_str = sys.stdin.read().replace(' ', '').replace('\n', '')
my_dict = {}
max_value = 0
max_list = []

for char in input_str:
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1

max_value = max(my_dict.values())
for k, v in my_dict.items():
    if v == max_value:
        max_list.append(k)
        
max_list = sorted(max_list)
for i in max_list:
    print(i, end = '')