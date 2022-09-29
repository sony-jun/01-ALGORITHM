T = int(input())
height = 0
top_height = 0
road = list(map(int,input().split()))       # 입력값을 리스트로 정렬 
for a in range(T):                          # 인덱스로 활용할 a 추출
    if road[a] < road[a + 1]:               # 리스트의 입력값을 그 다음 값과 비교하여 다음 값이 더 크다면,
        height += (road[a + 1] - road[a])   # height 라는 임시저장 변수에 그 차이만큼 더함
        if top_height < height:             # 동시에 top_height변수보다 height변수가 더 크다면
            top_height = height             # top_height에도 할당
    else:                                   # 리스트의 입력값이 그 다음 값보다 크다면
        if top_height < height:             # 오르막길이 끝난 것이기 때문에 기록된 height와 top_height를 비교하여 
            top_height = height             # 더 큰 수를 top_hegiht에 기록하고
        height = 0                          # height는 다시 0으로 초기화시켜준다.

    if a + 2 == T:                          # a가 마지막 값에 도달하면 비교할 다음 인덱스가 없어지기 때문에
        break                               # 마지막 값 바로 직전 값에 도달하면 반복문을 강제 종료한다.

print(top_height)                           # 기록된 가장 높은 오르막길을 출력