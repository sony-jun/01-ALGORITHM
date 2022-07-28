# https://www.acmicpc.net/problem/3052

list_ = []

for i in range(10):
    list_.append(int(input())%42)
print(len(set(list_)))
 