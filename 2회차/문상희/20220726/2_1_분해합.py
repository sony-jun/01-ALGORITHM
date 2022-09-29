n = int(input())

num_list = []

for i in range(n):
    sum_i = 0
    for j in str(i):
        sum_i += int(j)   
    if i + sum_i == n:
        num_list.append(i)
        
if num_list == []:
    print(0)
else:
    print(min(num_list))