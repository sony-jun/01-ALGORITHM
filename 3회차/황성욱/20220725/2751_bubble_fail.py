n = int(input())
num_list = []
for i in range(n):
    num = int(input())
    num_list.append(num)
for j in range(len(num_list)):
    for k in range(len(num_list)-j):
        if num_list[k] > num_list[k+1]:
            num_list[k], num_list[k+1] = num_list[k+1], num_list[k]
for x in num_list:
    print(x)