# https://www.acmicpc.net/problem/2577
# 백준 2577
# 세 자연수 A,B,C input
# A*B*C의 결과에 0-9 각각의 숫자가 몇번씩 쓰였는가
import sys
sys.stdin = open("0_숫자의개수.txt")
# input데이터를 보니 숫자가 한줄에 하나씩 입력되네요.
# 같은 형식으로 세번 입력되게 해줍니다.
A = int(input())
B = int(input())
C = int(input())
# print(A,B,C,sep=' ')
# A*B*C를 곱한 값에 있는 0-9까지 각각의 숫자 갯수를 추적해야하니까 
# 곱한 값을 문자열로 바꾸고 0-9랑 대조해보는게 편하겠어요.
result = str(A*B*C)
# range로 i를 0-9까지 10개를 가지는 배열로 문자열 result안의 숫자를 count할게요.
for i in range(10):
    # print(i,type(i)) # i = 0~9, type(int)
    # result는 문자열이니까 i도 같은 타입으로 바꿔야합니다.
    print(result.count(str(i)))

