# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

n = int(input())

for i in range(n):
    ox_list = list(input())  #list로 입력받기

    #OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점
    cnt = 0
    ox_cnt = 0
    for ox in ox_list: 
        if ox == 'O':      #변수가 O라면
            cnt += 1       # 1을 더해준다.
            ox_cnt += cnt  # O가 연속되면 점수가 1점씩 커진다.
        else:       #아니면
            cnt = 0 #0점 추가

    print(ox_cnt)
# 10
# 9
# 7
# 55
# 30





import sys
sys.stdin = open("3_OX퀴즈.txt")
T = int(input())
# test_case돌때마다 출력하는게 아니라 출력을 한번에 뱉어야하네요.
# 빈 리스트를 만들고 result를 집어넣어 리스트가 다 완성된 후 출력해줍시다.
for test_case in range(T):
    A = input()
    # i로 A를 읽어서
    result = 0
    c = 0
    for i in A:
        # O가 나올 때 c의값을 1씩 증가시키면서 c의 값을 다른 변수에 더한다.
        # O가 나오지 않으면 c의 값을 초기화시키기.     
        # print(i,end='')
        if i == 'O':
            c += 1
            result += c
        else : 
            c = 0
    print(result)