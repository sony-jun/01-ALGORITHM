# 직사각형 네개의 합집합의 면적 구하기 🐳
# 문제 : 좌표로 입력된 직사각형의 면적 구하기
#       (모든 x좌표와 y좌표는 1이상이고 100이하인 정수)

note = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            note[x][y] = 1

total = 0
for row in note:
    total += sum(row)

print(total)
