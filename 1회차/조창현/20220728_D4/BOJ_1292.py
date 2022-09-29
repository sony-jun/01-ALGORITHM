num_list = []

## 이걸 while 문으로 길이 조건을 주면 더 좋을거야!
for i in range(50):
    num_list += [i] * i
print(num_list)

sta_num, end_num = map(int, input().split())
# sta, end = 999, 1000
sum_num = 0

for i in range(sta_num - 1, end_num):
    sum_num += num_list[i]
print(sum_num)