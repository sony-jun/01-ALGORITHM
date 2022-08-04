# n = int(input())
# s = []
# cnt_h = 0
# cnt_v = 0
# position_h = 0
# position_v = 0
# for i in range(n):
#     s.append(input())
# for i in s:
#     for j in i:
#         if j == '.':
#             cnt_h += 1
#         else:
#             if cnt_h > 1:
#                 position_h += 1
#             cnt_h = 0
#     if cnt_h > 1:
#         position_h += 1
#     cnt_h = 0
# for i in range(n):
#     for j in range(n):
#         if s[j][i] == '.':
#             cnt_v += 1
#         else:
#             if cnt_v > 1:
#                 position_v += 1
#             cnt_v = 0
#     if cnt_v > 1:
#         position_v += 1
#     cnt_v = 0
# print(position_h, position_v)


n = m = int(input())

room = [list(input()) for _ in range(n)]
# pprint(room)
good_bed1 = 0   # 가로 누울자리
good_bed2 = 0   # 세로 누울자리
for i in range(n):
    cnt1 = 0
    cnt2 = 0
    for j in range(n):
        # 1번 if(가로)
        if room[i][j] =='.':        # 빈칸 이면 카운트 +1
            cnt1 += 1
        elif room[i][j] =='X':      # X가 나오면 누적카운트가 누울수 있는 2칸 이상인지 확인
            if cnt1 >= 2:           # 2칸 이상이면 누울자리로 카운트 +1
                good_bed1 += 1      
            cnt1 = 0                # 누울자리에 올렸으니 카운트는 초기화
        
        #2번 if(세로)
        if room[j][i] =='.':
            cnt2 += 1
        elif room[j][i] =='X':
            if cnt2 >= 2:
                good_bed2 += 1
            cnt2 = 0
        
        #3번 if(행렬의 끝)
        if j == (n-1):
        #행렬이 끝나는 반복중인 j와 입력값 n-1
            if cnt1 >= 2:
                good_bed1 += 1
            if cnt2 >= 2:
                good_bed2 += 1
        
    print(f'{good_bed1} {good_bed2}')