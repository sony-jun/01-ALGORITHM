# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input()) #150
b = int(input()) #266
c = int(input()) #427

val_multiply = str(a*b*c)         #순회하기 위해 문자열타입으로 변경


for num in range(10):             # 0 부터 10까지 반복할것 
    str_num = str(num)            # 비교하기 위해 문자열 타입으로 변경
    result = 0                    #값 저장할 변수
    for val_num in val_multiply:  #val_num에 abc곱한 값 순회
        if str_num == val_num:    #두 변수가 같다면 결과에 1추가하고 출력
            result += 1
    print(result)

