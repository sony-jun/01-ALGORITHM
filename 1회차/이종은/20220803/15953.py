# 상금헌터 

# 첫번째
first_place = [1, 3, 6, 10, 15, 21] # 각각 인덱스 매칭 
first_money = [500, 300, 200, 50, 30, 10]

# 두번째
second_place = [1, 3, 7, 15, 31]
second_money = [512, 256, 128, 64, 32]


for _ in range(int(input())): # 첫줄 숫자 반복
    a_money = []
    b_money = []

    a, b = map(int, input().split()) 
    for f in first_place: 
        if a > 21 or a == 0: # a가 순위 안에 포함되지 않거나 0일 때
            a_money = [0]
        elif a <= f: # a가 등수 구간에 있는지 체크 
            a_money.append(first_money[first_place.index(f)]) # 등수 안에 있다면, 그 인덱싱 값에 해당하는 상금 인덱싱 값 출력하고 리스트에 쌓음
        # 리스트 쌓는 이유: 구간에 있는지 체크하지만 예를 들어 8 경우에는 8이 작은 것이 뒤에도 포함 되기 때문에 더 작은 것에도 포함 되어있기 때문에 
    for s in second_place:
        if b > 31 or b == 0: # b가 순위 안에 포함되지 않거나 0일 때
            b_money = [0]
        elif b <= s:  # a가 등수 구간에 있는지 체크
            b_money.append(second_money[second_place.index(s)])
    print((max(a_money) + max(b_money)) * 10000) #각 리스트의 최댓값 구해서 더함
