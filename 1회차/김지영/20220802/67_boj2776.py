# 연종 : 하루동안 본 정수 모두 기억
# 수첩 1 : 연종이가 하루동안 본 모든 정수 기록
# M : 연종에게 질문
# x라는 정수를 오늘 본 적이 있는가?
# 수첩 2: 연종이 본적 있다 대답한 정수 기록
# 수첩 2 기준 수첩 1에 있으면 1, 없으면 0 출력
import sys
sys.stdin = open("input.txt")
T = int(input())
for test_case in range(1,T+1):
    note_1 = int(input())
    note_1_numbers = set(map(int,input().split()))  # 탐색시간 줄이는 중복제거
    note_2 = int(input())
    note_2_numbers = map(int,input().split())

    for n in note_2_numbers:
        if n in note_1_numbers:
            result = 1
        else : result = 0
        print(result)