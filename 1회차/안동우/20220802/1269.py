from re import A, T
import sys
sys.stdin = open("1269.txt", "r")
# input = sys.stdin.readline

A,B=map(int,input().split())
A_element=set(list(map(int,(input()).split())))
B_element=set(list(map(int,(input()).split())))
C=A_element^B_element#대칭차집합 C할당하고
print(len(C))# C길이출력
        
