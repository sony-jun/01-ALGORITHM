# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

 
#문제

# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 

# 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다

# 1. 자연수 a,b,c를 받기위해 input()함수 사용.
# 2. a x b x c를 곱한다.
# 곱한 값에 숫자들을 카운트 해야한다.
# 그렇다면 사용할 수 있는것은? 문자열로 변환? 리스트?


 # a, b, c에 자연수를 받아준다

a = int(input())
b = int(input())
c = int(input())


multiple = list(str(a * b * c)) # 받은 a b c의 곱을 문자열로 변환하고 리스트를 만들어준다



for count in range(10): #0~9까지
    print(multiple.count(str(count)), end=" ")# 0~9까지의 길이를 문자열로 변환후 리스트안에 0~9를 세줘