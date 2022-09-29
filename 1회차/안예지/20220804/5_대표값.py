# 2592.
"""



"""
num_list = list(input() for _ in range(10))
# num_list = ['10', '40', '30', '60', '30', '20', '60', '30', '40', '50']
num_avg = sum(map(int, num_list))//10
print(num_avg)

num_dict = {}
for i in num_list:
    num_dict[i] = num_dict.get(i, 0) + 1
max_r = max(num_dict.values())
for num in num_dict:
    if num_dict[num] == max_r:
        print(num)
