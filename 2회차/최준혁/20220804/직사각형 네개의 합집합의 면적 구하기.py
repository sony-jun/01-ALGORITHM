from pprint import pprint
# 100x100의 도화지를 그린다.
flat = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4): # 4번 반복하면서 
    # 왼쪽 아래 x, y 오른쪽 위 x, y 좌표값 입력받기 
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2): # 왼쪽아래 x 부터 오른쪽 위 x 까지
        for j in range(y1, y2): # 왼쪽아래 y부터 오른쪽 위 y까지
            flat[i][j] = 1 # 해당하는 부분을 1처리

result = 0 # 합계값을 받을 result
for k in flat:
    result += sum(k) # 1로 처리된 면적 전부 합산
print(result) # 출력