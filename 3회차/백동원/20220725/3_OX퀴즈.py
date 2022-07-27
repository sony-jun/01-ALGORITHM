# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())                
for i in range(1, T + 1):       
    test_case = list(input())  # 입력받은 OX 문제를 하나하나 쪼개어 리스트에 저장한다.
    result = 0                  # 결과값은 매 문제마다 다르니 시작시에 초기화할 수 있게 한다.
    point = 1                   # 포인트 시작값은 1이다.
    for OX_judge in test_case:  # 리스트로 쪼갠 OX문제에서 처음부터 하나씩 순회한다.
        if OX_judge == 'O':     # O가 나오면 
            result += point     # 결과값에 포인트를 추가한다. 
            point += 1          # 다음 결과값이 0인것을 대비하여 미리 포인트에 1을 더한다.
        else:                   # X가 나오면 
            point = 1           # 포인트는 1로 고정한다.
    print(result)