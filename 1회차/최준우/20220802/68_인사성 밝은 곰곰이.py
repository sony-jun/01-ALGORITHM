# https://www.acmicpc.net/problem/25192

import sys
input = sys.stdin.readline

N = int(input()) # 채팅방 기록 수
chat_dict = {} # 사람이름을 담을 딕셔너리

cnt = 0 # 총 인사 수 를 합산할 변수
for i in range(N): # N번만큼 반복
    name = input().rstrip()
    if name != 'ENTER': # 입력된게 'ENTER'가 아닌 사람이름일때
        if name not in chat_dict: # 기존에 인사를 안했으면, value를 1로
            chat_dict[name] = 1
    else:# 'ENTER' 일떄, 입장. 딕셔너리를 초기화 하기전에 value가 1이었던 사람 cnt+1
        for k, v in chat_dict.items():
            if v == 1:
                cnt += 1
        chat_dict = {} # 초기화

for k, v in chat_dict.items(): # 마지막번째에서, value가 1인사람들 수 cnt에 +1
    if v == 1:
        cnt += 1
print(cnt) # 총 cnt 출력= 1
print(cnt)