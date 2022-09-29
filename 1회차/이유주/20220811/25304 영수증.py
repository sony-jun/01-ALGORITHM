#구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 보는 프로그램
import sys
sys.stdin = open("input.txt")

#구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 보는 프로그램

price = []
X = int(input()) #영수증 총금액
N = int(input())  #구매한 물건의 종류 수
for i in range(N):
    a, b = map(int,input().split()) #a-물건의 가격,b-개수
    price.append(a * b)

if sum(price) == X:
    print("Yes")

else:
    print("No") 
