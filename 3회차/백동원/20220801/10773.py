T = int(input())
number_list = []
for _ in range(T):
    a = int(input())
    if a != 0:
        number_list.append(a)
    else:
        number_list.pop()
print(sum(number_list))