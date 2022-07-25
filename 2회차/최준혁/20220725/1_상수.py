# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("/Users/mac/Desktop/TIL/01-ALGORITHM/2회차/최준혁/20220725/1_상수.txt")

A, B = sys.stdin.readline().split()
rev_A = list(reversed(A)) # 입력받은 값을 뒤집고 리스트에 담는다
rev_B = list(reversed(B))
a = '' # 뒤집은 값을 형변환 후에 비교하기 위해 생성 
b = ''
for i in range(3): # 리스트 0,1,2 범위
    a += rev_A[i]  
    b += rev_B[i]

if int(a) > int(b):
    print(a)
else:
    print(b)
    
    

