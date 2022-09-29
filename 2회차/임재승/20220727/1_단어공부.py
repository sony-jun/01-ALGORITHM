# https://www.acmicpc.net/problem/1157

T = input().upper()
set_T = list(set(T))

cnt_list = []

for idx in set_T:
    cnt = T.count(idx)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(set_T[cnt_list.index(max(cnt_list))])