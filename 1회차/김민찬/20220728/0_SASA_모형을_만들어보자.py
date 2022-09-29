N, M = map(int, input().split())

count = min(N, M) # 2개의 수 중 작은 값을 선택
# S * 2 + A * 2 = 1 set
print(count // 2) # S와 A 두 개씩 필요하니 2로 나눠준다.