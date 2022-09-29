import sys
input = sys.stdin.readline

a, b =map(int, input().split())  #a와 b의 원소의 개수
A = set(list(map(int, input().split())))  #A집합
B = set(list(map(int, input().split())))  #B집합

print(len(A ^ B))  #대칭차집합 ^