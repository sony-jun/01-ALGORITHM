# https://www.acmicpc.net/problem/2908
import sys
sys.stdin = open("1_상수.txt")
# input data를 보니 세자리 수 두개가 띄어쓰기로 구분되어 입력됩니다.
a, b = input().split()
# 상수는 수를 뒤집어서 큰쪽을 말할거에요.
# 입력받은 값 그대로 str을 뒤집어서 정수 값으로 변환하여 비교해준 후, 
# 큰쪽을 다시 뒤집어서 말해줍니다.
# list였다면 그냥 reverse() 함수를 사용하면 되겠지만, 
# str이니 뒤집은 후 join해줍니다.

# before code review
# A = ''.join(reversed(A))
# B = ''.join(reversed(B))
# if int(A) > int(B):
#     print(A)
# else : print(B)
# print(A,B,type(A),type(B)) # 확인용


# after code review
a = int(a[::-1]) #734  --> 437
b = int(b[::-1])
print(a if int(a)>int(b) else b)
