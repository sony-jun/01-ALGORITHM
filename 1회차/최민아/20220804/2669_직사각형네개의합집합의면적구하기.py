import sys
sys.stdin = open("20220804/2669_직사각형네개의합집합의면적구하기.txt")

nemo = []
for r in range(4):                          # 4개의 직사각형
    a, b, c, d = map(int, input().split())  # 좌표 입력 받음
    for i in range(a, c):                   # 가로
        for j in range(b, d):               # 세로
            nemo.append((i, j))             # 직사각형의 면적을 1칸씩 쪼개서 좌표 저장

area = set(nemo)                            # 중복되는 칸(좌표) 제거

print(len(area))                            # 남는 칸의 개수 출력