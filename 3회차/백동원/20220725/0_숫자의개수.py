# # https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")
A = int(input())
B = int(input())
C = int(input())
result = A * B * C                      
result_number = []
while result != 0:                      
    result_number.append(result % 10)   # 반복문을 활용하여 결과값을 10으로 나눈 나머지를 리스트에 추가하고
    result //= 10                       # 결과값에 10으로 나눈 몫을 다시 할당하여 결과값이 0이 되면 멈춘다.
for i in range(10):                     # 0에서 9까지 순회하기 위해 for문과 range를 사용했고
    print(result_number.count(i))       # 리스트의 숫자들이 몇 개가 존재하는지 count 메소드를 활용하여 순서대로 출력한다.