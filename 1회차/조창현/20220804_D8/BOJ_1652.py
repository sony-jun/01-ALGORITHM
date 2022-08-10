from pprint import pprint
import sys

sys.stdin = open('1652.txt')

n = int(input())
hori_room = [list(map(str, input())) for i in range(n)]
pprint(hori_room)
hori_cnt = 0
for r in range(n):
    hori_list = ''.join(hori_room[r]).split('X')
    print(hori_list)
    for i in range(len(hori_list)):
        if '..' in hori_list[i]:
            hori_cnt += 1

verti_cnt = 0
verti_room = []
for c in range(n):
    temp_list = []
    for r in range(n):
        temp_list.append(hori_room[r][c])
    verti_room.insert(c, temp_list)
#pprint(verti_room)

for r in range(n):
    hori_list = ''.join(verti_room[r]).split('X')
    for i in range(len(hori_list)):
        if '..' in hori_list[i]:
            verti_cnt += 1

print(f'{hori_cnt} {verti_cnt}')
            