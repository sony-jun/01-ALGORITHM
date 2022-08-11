# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.
import sys
sys.stdin = open("25304.txt")

X = int(input())
N = int(input())
sum_ab=0
for i in range(N):
    a,b = map(int,input().split())
    sum_ab+=a*b
if X == sum_ab:
    print("Yes")
else:
    print("No")