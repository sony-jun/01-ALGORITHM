# 25192.
"""
새로운 사람이 입장한 이후 처음 채팅을 입력하는 사람은 반드시 곰곰티콘으로 인사를 한다.

# 접근 방법
1. 채팅기록을 set으로 받는다.
2. ENTER가 아닌 name이 들어오면 set에 추가한다
3. ENTER 가 나오면 현재까지의 set의 길이를 총 곰곰 횟수에 더하고 set을 초기화한다.
4. 마지막 시행 때 지금까지 누적된 총 곰곰횟수와 해당 시행 때의 set 길이를 더한다

"""
import sys
# input = sys.stdin.readline
sys.stdin = open("곰곰이.txt")

# N = int(input())
# # gom 나온 횟수 저장 변수
# gom = 0
# name = set()
# for _ in range(N):
#     # 채팅기록을 받아오는 변수
#     clog = input()
#     if clog != 'ENTER':
#         name.add(clog)
#     else:
#     # ENTER라면
#         gom += len(name)
#         name.clear()
# print(gom + len(name))

N = int(input())
name = set()
gom = 0
for _ in range(N):
    log = input()
    if log == 'ENTER':
        name.clear()
    elif log != 'ENTER':
        if log not in name:
            name.add(log)
            gom += 1
print(gom) 
