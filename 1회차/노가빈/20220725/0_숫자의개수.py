# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")
a = int(input()) #한 줄씩 읽어들인 게 변수에 들어간다.
b = int(input())
c = int(input())
sum = a*b*c
sumList = list(map(int, str(sum))) #숫자를 리스트로 변경

num_count = {}
for num in sumList:
    num_count[num] = 0 # 특정 문자 딕셔너리에 추가
for num in sumList:
    num_count[num] = num_count[num] + 1 # 추가한 딕셔너리에서 갯수 더하기
for key, value in num_count.items(): # 키와 값 모두 출력
    print(key)
    print(value)