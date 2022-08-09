# 몬스터 트럭 🐳
# 문제 : 혜빈이 차의 온전한 주차 공간과 주차 공간을 사용하는데 부숴야 하는 차의 개수 구하기

R, C = map(int, input().split())

parking = [list(input().strip()) for _ in range(R)]

all, one, two, three, four = 0, 0, 0, 0, 0
for i in range(R - 1):  # 인덱스 벗어나지 않게 설정
    for j in range(C - 1):

        arr = []
        for x in range(2):  # 혜빈이의 차 크기
            for y in range(2):
                arr.append(parking[i + x][j + y])

        if '#' in arr:  # '#'은 건너뛰기
            continue

        if arr.count('.') == 4:  # 리스트 안에 주차공간을 확인하해서 카운팅
            all += 1
        elif arr.count('X') == 4:
            four += 1
        elif arr.count('X') == 3:
            three += 1
        elif arr.count('X') == 2:
            two += 1
        elif arr.count('X') == 1:
            one += 1

print(all, one, two, three, four, sep='\n')
