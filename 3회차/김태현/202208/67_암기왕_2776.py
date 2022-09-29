import sys
sys.stdin = open("67_암기왕_2776.txt", "r")

T = int(input())

N = int(input())
one_list = set(map(int, input().split()))

M = int(input())
two_list = set(map(int, input().split()))

for j in two_list:
    if j in one_list:
        print(1)
    else:
        print(0)
