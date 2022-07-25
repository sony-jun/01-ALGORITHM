# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input()) 
for i in range(T):  #테스트케이스만큼 확인하니까
    answer = input() 
    total = 0
    point = 0
    for i in answer:   # OXOOX 이런걸 하나하나 순회
        if i == 'O': # i가 O일떈 포인트 1점추가, 총점은 포인트의 누적이니 포인트를 추가
            point += 1
            total += point
        if i != 'O':  # 포인트는 X가 나오면 0점으로 돌아감
            point = 0
    print(total) # 총점을 출력
