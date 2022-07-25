# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A,B = map(int , input().split())
A_list = []
B_list = []
A_list.extend(str(A))
B_list.extend(str(B))
A_list.reverse()
B_list.reverse()

A = ''.join(A_list)
B = ''.join(B_list)

print(max(A,B))