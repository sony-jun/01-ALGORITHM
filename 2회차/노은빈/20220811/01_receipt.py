import sys
sys.stdin = open("receipt.txt")

x = int(input()) #총 금액
n = int(input()) #물건의 종류
cost = [] #가격 리스트

for i in range(n):
    a, b = map(int,input().split())
    c = a*b
    cost.append(c) #가격 리스트에 곱한 값 추가
#print(cost)
    total_cost = sum(cost) #가격의 총합
# print(total_cost)   
if total_cost == x: #가격의 총합이 x와 같다면
    print('Yes')
else :  #아니라면
    print('No')
