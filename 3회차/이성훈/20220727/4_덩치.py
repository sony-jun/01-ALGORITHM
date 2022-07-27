# https://www.acmicpc.net/problem/7568
import sys

sys.stdin = open("4_덩치.txt")

T = int(input())                                        #사람의 수
T_list = []
for i in range(T):
    weight, height = list(map(int,input().split()))
    T_list.append((weight,height))

print(T_list)
for i in T_list:
    rank = 1
    for j in T_list:
        if i[0] <j[0] and i[1] <j[1]:
            rank += 1
    
    print(rank, end = " ")
