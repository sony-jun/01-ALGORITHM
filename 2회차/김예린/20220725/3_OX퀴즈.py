# https://www.acmicpc.net/problem/8958
#import sys

t = int(input())
for test_case in range(1, t + 1): # 테스트 케이스 횟수
    
    ox_list = list(input()) # 입력한 OX를 리스트로 만들어준다. 
    cnt = 0
    result = 0
    for i in ox_list:       # i에 O,X가 차례대로 들어온다. 
        if i == 'O':        # 만약 i에 O가 들어왔다면 
            cnt += 1        # cnt에 1을 추가한다
            result += cnt      # cnt의 값을 fin에 넣어준다. 
                            # 연속적인 O가 들어오는 경우 cnt는 1씩 늘어나기 때문에
                            # 연속적인 숫자 (1+2..) 합계가 가능하다. 
        else:
            cnt = 0         # X가 i에 들어오는 경우, cnt를 0으로 비워준다. 
    
    print(result)
#sys.stdin = open("3_OX퀴즈.txt")

