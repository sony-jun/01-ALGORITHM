from re import A
import sys

sys.stdin = open("04.우유축제.txt")

T = int(input()) #우유 가게 수 입력 받아서
milk_store = list(map(int,input().split())) 
# 우유 가게 정보 입력받기(리스트)

count = 0 
# 마신 우유 수를 저장한 변수 count

for i in range(T): #for문으로 우유 가게를 순회하면서
    if milk_store[i] == count % 3: 
# 0->1->2 순서로 마셔야 하기 때문에 milkstore를 나머지 연산(3으로 나눈 나머지)으로 처리.
# 우유 가게에서 파는 우유(ex,딸기0,초코1,바나나2)와 마실종류가 같다면 +1
        count += 1

print(count)

# input값
# 7
# 0 2 2 0 1 2 3 으로 하니 4 나왔음.