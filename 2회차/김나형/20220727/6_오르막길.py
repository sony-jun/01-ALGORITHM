import sys

sys.stdin = open("6_오르막길.txt")

N = int(input())
list_way = list(map(int, input().split()))
start, end = list_way[0], list_way[0] # start와 end 변수 값을 list의 0번째 배열로 정함
high = 0

for i in range(1, N): # 0번째 배열을 뺀 1~N과 하나씩 비교
    if end >= list_way[i]: 
        start = list_way[i]
        end = list_way[i]
         
    else:
        end = list_way[i]
    high = max(high, end - start)

print(high)