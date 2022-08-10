# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
import sys

sys.stdin = open("14_나머지.txt")


num = 0
num_1 = []

for i in range(10): # 정수를 10 번 받아온다.
    num = int(input()) # num에 input 값 입력
    num_1.append(num % 42)  # 42로 나누어 리스트에 저장
print(len(set(num_1))) # set으로 중복값 제거 >> 서로 다른 값만 출력