# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")


A = int(input())
B = int(input())
C = int(input())

re = A * B * C

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #인덱스 0~9 리스트 초기화

for i in str(re):    #세 합을 곱한 값을 str로 
    count[int(i)] +=1

for j in count:
    print(j) 
    