sum_list = []

for i in range(5):
    num = sum(map(int, input().split()))
    sum_list.append(num)

print(sum_list.index(max(sum_list))+1, max(sum_list))