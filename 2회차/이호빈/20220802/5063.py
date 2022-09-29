#입력값 받기
N = int(input())

for _ in range(N):
    #입력값을 받기
    ad = list(map(int, input().split()))

    # 리스트 1번째 요소에서 2번째 요소를 뺀 것이 0번째 요소보다 크다면 advertise
    if ad[0] < ad[1] - ad[2]:
        print("advertise")
    # 리스트 1번째 요소에서 2번째 요소를 뺀 것이 0번째 요소보다 같다면 does not matter
    elif ad[0] == ad[1] - ad[2]:
        print("does not matter")
    # 리스트 1번째 요소에서 2번째 요소를 뺀 것이 0번째 요소보다 같다면 do not advertise
    else:
        print("do not advertise")