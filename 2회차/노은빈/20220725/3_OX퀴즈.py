# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

t = int(input())

for i in range(t) :  #변수 t만큼 반복
    lst = list(input())  #input을 리스트 값으로 
    cnt = 0  #0부터 리스트 안의 값 개수 세기
    sum = 0  #합계

    for i in lst :  
        if i == 'O' :  #만약 'o'가 있으면 
            cnt += 1   # +1
            sum += cnt  #합계도 개수만큼 더함
        else :
            cnt = 0   #'X'라면 0 더함
    print(sum)
