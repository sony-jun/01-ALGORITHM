# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")



a = int(input())           # 세 정수 입력
b = int(input())
c = int(input())

dic = {}                   # 딕셔너리로 키:값 쌍으로 구현

s = a*b*c                  # s = 세 정수의 곱

for i in range(10):
    dic[str(i)]=0          # 0~9 까지의 키 생성 및 초기값0 입력

for char in str(s):
    dic[char] += 1         # 세 정수의 곱 결과값에 한자리씩 접근하여 횟수 카운트
    
for n in range(10):
    print(dic[str(n)])     # 딕셔너리 키가 0~9 순서대로 값 출력 