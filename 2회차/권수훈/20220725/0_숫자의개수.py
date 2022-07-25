# https://www.acmicpc.net/problem/2577
from itertools import count
import sys
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
A = int(input())
B = int(input())
C = int(input())
# 3개의 정수를 한번씩 입력받기 위해 int(input())을 3번했다.
lists= str(A*B*C)
# 입력받은값을 곱한결과값을 문자열로 하나씩 정리하고싶어서 str 하여 lists에 저장했다
for result in range(10): 
   print(lists.count(str(result))) #result 를 문자열로 바꿔서 몇개가있는지 카운트함




# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
sys.stdin = open("0_숫자의개수.txt")
