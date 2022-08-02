# https://www.acmicpc.net/problem/1269
import sys

sys.stdin = open("0_대칭 차집합.txt")

N = map(int,input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

A_B = len(A - B)
B_A = len(B - A)

print(A_B + B_A)
