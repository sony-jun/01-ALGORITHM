# https://www.acmicpc.net/problem/2750
import sys

sys.stdin = open("3_수 정렬하기.txt")
T = int(input())
list_ = []

for i in range(T):
    num = int(input())
    list_.append(num)

list_.sort()
for i in list_:
    print(i)
    
