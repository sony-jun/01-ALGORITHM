# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = map(int,input().split())  #두수가 띄어쓰기로 주어지니

revA = int(str(A)[::-1])  #수를 뒤집기위해 요소하나하나를 읽을수있는 스트링으로 변환후 뒤집고 다시 정수로변환
revB = int(str(B)[::-1])

if revA > revB:   #큰수를 말하는거니까
    print(revA)
else:
    print(revB)