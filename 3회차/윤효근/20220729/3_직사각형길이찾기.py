import sys

sys.stdin = open("직사각형 길이 찾기.txt", "r")

T = int(input())

for test_case in range(1, T + 1):

    a=list(map(int,input().split()))

    for i in a:
        if a.count(i) <= 1:             #직사각형은 2변의 길이가 같기 때문에 같은 변의 길이가 없는 값을 찾는다
            print(f'#{test_case} {i}')

        elif a.count(i) >= 3:           #정사각형은 모든 변의 길이가 같기때문에 3변이 다 같은지 검사한다
            print(f'#{test_case} {i}')
            break