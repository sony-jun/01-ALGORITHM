# R = 행의 개수
# C = 열의 개수
R, C = map(int, input().split())

parking_lot = []
for _ in range(R):
    parking_lot.append(input())

n_zero = 0
n_first = 0
n_second = 0
n_third = 0
n_fourth = 0

for r in range(R):
    for c in range(C):
        if r+1 == R or C+1 == C:
            break
        w = parking_lot[r][c]
        x = parking_lot[r][c+1]
        y = parking_lot[r+1][c]
        z = parking_lot[r+1][c+1]

        tmp = W+X+Y+Z

        if "#" in tmp: # 만약 빌딩이면 계속 실행
            continue
        else:
            n_car = tmp.count("X")
            if n_car == 0:
                n_zero += 1
            elif n_car == 1:
                n_first += 1
            elif n_car == 2:
                n_second += 1
            elif n_car == 3:
                n_third += 1
            elif n_car == 4:
                n_fourth += 1

print(n_zero) # 첫째 줄 출력
print(n_first)
print(n_second)
print(n_third)
print(n_fourth)