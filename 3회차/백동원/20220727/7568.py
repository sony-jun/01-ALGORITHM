T = int(input())
number_list = []
dungchi =[]
for a in range(T):
    number_list.append(list(map(int, input().split()))) # 리스트 내에 리스트로 받는다.

for b in number_list:
    cnt = 0
    for c in number_list:                   # 이중 for 문으로 
        if b[0] < c[0] and b[1] < c[1]:     # 나보다 덩치가 작은 사람 수를 카운트
            cnt += 1
    dungchi.append(cnt + 1)                 # 나의 등수는 나보다 덩치가 작은 사람 수 + 1 이므로
                                            # 계산해서 리스트에 추가
for d in dungchi:                           # 순서대로 출력하되       
    print(d, end = ' ')                     # 띄어쓰기 대신 공백으로

# tier_list = []
# for d in dungchi_over:
#     tier_cnt = 0
#     for e in dungchi_over:
#         if d < e:
#             tier_cnt += 1
#     tier_list.append(tier_cnt + 1)