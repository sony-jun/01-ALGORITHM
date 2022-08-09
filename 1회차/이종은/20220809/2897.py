# 몬스터 트럭

n ,m = map(int, input().split()) # 행의 개수, 열의 개수 입력

parking = [] # 빈 리스트 생성

for _ in range(n): # 행의 개수만큼 반복
    parking.append(input()) # 문자열 입력 받은 것을 parking리스트에 추가

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0

for i in range(n): # 행의 개수만큼 반복 
    for j in range(m): # 열의 개수만큼 반복(2차원 배열 생성)
        if i+1 == n or j+1 == m: # 배열의 끝을 넘어가면 안됨으로,,? (3,0), (0,3)
            break
        a = parking[i][j] # (0,0) # (2, 2)정사각형 탐색
        b = parking[i][j+1] #(0,1)
        c = parking[i+1][j] #(1,0)
        d = parking[i+1][j+1] #(1,1)

        tmp = a+b+c+d # 탐색한 것을 바탕으로 배열만듬

        if "#" in tmp: # 빌딩이 있으면
            continue # 실행되다가 continue를 만나면 그 아래 코드를 수행하지 않고 for문으로 넘어감 
        else: # "#"(빌딩)이 없을 때
            n_car = tmp.count("X") # Temp 문자열에서 x의 개수 카운트
            if n_car == 0: # x가 0이면 아무 차도 안부심
                n1 += 1 # 1
            elif n_car == 1:
                n2 += 1
            elif n_car == 2:
                n3 += 1
            elif n_car == 3:
                n4 += 1
            elif n_car == 4:
                n5 += 1
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)


