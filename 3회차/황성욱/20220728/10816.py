n = int(input())
p_arr = list(map(int, input().split()))
m = int(input())
f_arr = list(map(int, input().split()))
f_dict = {}
li = [0] * m
# for f in f_arr:  # 키 중복 
#     f_dict[f] = 0
for p in p_arr:
    if p in f_dict:
        f_dict[p] += 1

for res in f_dict.values():
    print(res, end=' ')