import sys
sys.stdin = open("01_대칭차집합.txt", 'r')

N, M = [*map(int, sys.stdin.readline().split())]

A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

print(len(A ^ B))