# https://www.acmicpc.net/problem/2577

#count 함수 활용
#변수.count(찾는 요소)
#괄호 안에 찾고자 하는 값을 입력하면 변수 안에서 해당 값의 개수를 숫자로 반환한다.

import sys
sys.stdin = open('0_숫자의개수.txt')

a = int(input())
b = int(input())
c = int(input())
print('hello')

total = str(a * b * c)
for i in range(0, 10):
    print(total.count(str(i)))