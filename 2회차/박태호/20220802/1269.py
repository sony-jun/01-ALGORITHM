# 대칭 차집합
import sys
sys.stdin = open('1269.txt','r')

a, b = input().split()

a_num = set(map(int, input().split()))
b_num = set(map(int, input().split()))

print(len(a_num^b_num))