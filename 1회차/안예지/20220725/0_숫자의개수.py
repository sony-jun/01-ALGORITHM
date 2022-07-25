# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

"""
# 2577. 
세 개의 자연수 A, B, C가 주어질 때 A*B*C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번 쓰였는지를 구하는 프로그램 작성

# 입력
첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다.
A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수

# 출력
첫째 줄에는 A*B*C의 결과에 0이 몇 번 쓰였는지 출력한다.
마찬가지로 둘째 줄부터 열 번째 줄까지 1부터 9까지의 숫자가 몇 번 쓰였는지 차례대로 한 줄에 하나씩 출력한다.

"""
A = int(input())
B = int(input())
C = int(input())

# 숫자를 만날때마다 1을 카운트 시킬 리스트를 만든다.
number_list = [0] * 10
# A*B*C 값의 문자 형변환된 값을 순회하면서
for idx in str(A*B*C):
    # 바인딩된 문자와 같은 인덱스에 1을 추가한다
    number_list[int(idx)] += 1
    # 리스트를 순회하여 차례로 한 줄에 하나씩 출력한다
for i in range(len(number_list)):
    print(number_list[i])
