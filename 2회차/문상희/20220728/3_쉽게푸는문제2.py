pos_1, pos_2 = map(int, input().split())

pos_1_num = pos_1
for i in range(50):
    if pos_1_num -i > 0:
        pos_1_num -= i
    else:
        pos_1_num = i
        break
pos_2_num = pos_2
for i in range(50):
    if pos_2_num -i > 0:
        pos_2_num -= i
    else:
        pos_2_num = i
        break
if pos_1_num == pos_2_num:
    print(pos_2_num(pos_2-pos_1))
else:
    result = 0
    for i in range(pos_1_num + 1, pos_2_num):
        result += i*i
    result = result + pos_2_num
