from pprint import pprint

N = int(input())

room = [list(map(str, input())) for i in range(N)]
r_seat = 0
c_seat = 0
for r in range(N):
    cnt_r = 0
    cnt_c = 0
    for c in range(N):
        # 가로
        if room[r][c] == '.': # 빈자리일때 
            cnt_r += 1  # 카운트 1 증가
        else:
            cnt_r = 0 # 짐을 만나면? 초기화
        if cnt_r == 2: # 누울자리가 생기면
            r_seat += 1 # 누울자리 카운트 증가

        # 세로
        if room[c][r] == '.': # 빈자리일때
            cnt_c += 1 # 카운트 1 증가
        else:
            cnt_c = 0 # 짐을 만나면 초기화
        if cnt_c == 2: # 누울자리가 생기면 
            c_seat += 1 # 카운트 증가
print(r_seat, c_seat) # 가로 세로 출력
# pprint(room)
    
    


