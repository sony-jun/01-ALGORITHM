import sys

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

list_ = []
dict_ = {}

for i in range(1,N+M+1):
    list_.append(input())

for i in list_:
    if i in dict_:
        dict_[i] += 1
    else:
        dict_[i] = 1

people_list = [k for k, v in dict_.items() if v == 2]
people_list.sort()
print(len(people_list))

for i in people_list:
    print(i)
