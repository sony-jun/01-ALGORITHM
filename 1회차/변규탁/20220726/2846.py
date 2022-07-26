# 12 3 5 7 10 6 1 11
n = int(input())
road = list(map(int, input().split()))

height = 0
height_list = []

for i in range(1, n):
    if road[i] > road[i-1]:
        height += road[i] - road[i-1] 
        if i == n-1: # 계속 오르막길이다가 마지막길에 다다르면 리스트에 추가.
            height_list.append(height)
            
    else: # 처음 내리막길 나오면 전에 height에 저장해둔 값을 리스트에 저장하고 바로 초기화
        height_list.append(height)
        height = 0

print(max(height_list))
    
        