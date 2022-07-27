T = int(input())
number_list = []
dungchi_over =[]
for a in range(T):
    number_list.append(input().split())

for b in number_list:
    cnt = 0
    for c in number_list:
        if b[0] > c[0] and b[1] > c[1]:
            cnt += 1
    dungchi_over.append(cnt)

tier_list = []

for d in dungchi_over:
    tier_cnt = 0
    for e in dungchi_over:
        if d >= e:
            tier_cnt += 1
    tier_list.append(len(dungchi_over) - tier_cnt + 1)

for h in tier_list:
    print(h, end = ' ')