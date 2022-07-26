n = int(input())
road = list(map(int, input().split()))
# 오르막길 크키 넣을 임시 변수 0으로 초기화
tmp = 0
# tmp 값 넣을 list 생성
up = []

# 리스트 순회
for i in range(1, n):
    # 만약 리스트에 있는 현재 높이가 전 높이보다 크면
    if road[i] > road[i-1]:
        # tmp에 현재 높이에서 전 높이 뺀 값 더하기
        tmp += road[i] - road[i-1]

        # 만약 맨 마지막 높이면
        if i == n - 1:
            # up 리스트에 tmp 값 추가
            up.append(tmp)
    # 만약 리스트에 있는 현재 높이가 전 높이보다 작거나 같으면
    else:
        # 전까지 저장했던 tmp를 up에 추가
        up.append(tmp)
        # tmp를 0으로 초기화
        tmp = 0

# up 리스트에 있는 값 중 최대값 출력
print(max(up))