# https://www.acmicpc.net/problem/2577
#import sys

#sys.stdin = open("0_숫자의개수.txt")
A = int(input())
B = int(input())
C = int(input())
D = A * B * C #기본연산
number = [0]*10 #숫자마다 담은뒤 순서대로 정렬하기위함. 0~9까지 숫자의 개수를 넣을예정
for i in str(D): # D는 숫자니 순회가 안됨. 문자열로바꿈
    for j in range(10):  # 문자열 D를 요소마다 순회하면서 그게 0~9숫자중 어떤건지 확인하기위해 
        if j == int(i):  # 0~9중 숫자 하나인 j가, int(i) 와 같다면 리스트에 넣어줌.. 숫자를 1 추가해줌.
            number[j] += 1        

for i in number:
    print(i) # 리스트상태인 number의 요소를 각각 추출하기위함
        

