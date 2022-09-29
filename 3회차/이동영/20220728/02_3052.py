import sys

sys.stdin = open("input.txt", "r")

numbers_list = []
rest_list = [] 

for i in range(1,11):

    numbers_list.append(int(input()))

for j in numbers_list:

    rest_list.append(j % 42)

rest_set = set(rest_list)

print(len(rest_set))