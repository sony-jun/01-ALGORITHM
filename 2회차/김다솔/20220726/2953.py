import sys
sys.stdin = open('2953.txt', 'r')

sum_list = []
for i in range(5):
    # print(list(map(int, input().split())))
    sum_list.append(sum(map(int, input().split())))
    
# print(sum_list)
highest = max(sum_list)
print(sum_list.index(highest) + 1, highest)