# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

# 각각 한줄로 변수 A, B, C 를 받아야 하므로 각각 input을 한줄로 받기

A = int(input())
B = int(input())
C = int(input())

# 각각의 숫자에 해당되는 값의 개수를 기록하기위해 빈 리스트를 생성

number_cnt = list()

# 결과값을 문자열로 바꿔놓기

result = str(A*B*C)

# 빈리스트에 인덱스 0부터 9까지 0을 할당해놓기

for i in range(10):
    number_cnt.append(0)

# str의 result에서 i의 개수를 세기위해서 빈리스트의 해당 인덱스에 +1을 실행

for i in result:
    number_cnt[int(i)]+=1

# 완성된 리스트를 하나씩 출력
for i in number_cnt:
    print(i)