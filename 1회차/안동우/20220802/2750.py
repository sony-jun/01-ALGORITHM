import sys
import heapq
sys.stdin = open("2750.txt", "r")

N=int(input())
a=[]
for k in range(1,N+1):
    a.append(int(input()))#입력  a리스트추가
    a=sorted(a) #a리스트정렬 a할당
for i in range(len(a)):
    print(a[i])#요소출력