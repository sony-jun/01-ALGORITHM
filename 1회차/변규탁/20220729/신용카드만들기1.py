# 룬 공식이란 카드 마지막 자리(16번째) 숫자를 구하는 공식이다.

# 매 홀수자리마다 숫자 2를 곱해서 더하고
# 매 짝수자리는 그대로 더한다
# 이 두개를 더한 숫자에 N을 더한 숫자가 10으로 나눠떨어지면 유효

import sys

sys.stdin = open("예제입력.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    card = list(map(int, input().split()))

    fifteen = 0
    for i in range(1, len(card) + 1) :
        if i % 2 == 0:
            fifteen += card[i-1]
        else:
            fifteen += card[i-1]*2

    if fifteen % 10 == 0 :
        answer = 0
    else:
        answer = 10 - (fifteen % 10) 
    
    print(f'#{test_case} {answer}')
