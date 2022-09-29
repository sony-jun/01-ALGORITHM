import sys
sys.stdin = open("1. 영수증.txt", "r")

input = sys.stdin.readline

cost = int(input()) # 가격 입력
result = 0 # 구매한 품목 합
T = int(input())
for _ in range(T):
    a,b = map(int,input().split()) # 물건의 가격과 몇개 샀는지 입력
    result += a*b # 가격과 갯수 곱한 만큼 result에 더함.
if cost == result: # cost와 result 같으면
    print('Yes') # yes
else : 
    print('No') # 다르면 no