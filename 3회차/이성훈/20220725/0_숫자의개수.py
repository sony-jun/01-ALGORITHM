# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")
# 딕셔너리 key값 0~9까지 만듬
E = {'0' : 0, '1' : 0 ,'2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}
# 변수 A, B, C에 상수 값 입력 
A = int(input())
B = int(input())
C = int(input())

# 변수 D에 곲한값 저장
D = A*B*C
# 상수 D를 문자로 변환
str_D = str(D)
# 문자 D를 쪼깸
for i in str_D:
    # 딕셔너리E에 i(숫자)가 있다면 1증가
    if i in E:
        E[i] += 1
    else:
        E[i] = 1
# 0~9까지 Value값만 출력
for i in E:
    print(E[i])
    
