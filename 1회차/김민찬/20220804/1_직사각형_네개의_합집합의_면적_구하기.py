import sys

sys.stdin = open("1_직사각형_네개의_합집합의_면적_구하기.txt")

Matrix = [[0] * 100 for _ in range(100)] # 100 X 100 영행렬 생성
result = 0
for i in range(4): # x 시작, y 시작, x 끝, y 끝
    x1, y1, x2, y2 = map(int, input().split())

# 겹치는 면적(?)
# 아무런 값도 없는 x, y에 사각형이 한 번이라도 해당 면적에 속하면 1을 대입
# x, y에 해당 좌표에 있는 값이 1의 크기들을 더하면 면적이 된다.

    for j in range(x1, x2): # 색칠된 면적 구하기
        for k in range(y1, y2):
            if Matrix[k][j] == 0:
                Matrix[k][j] = 1
                result += 1
print(result)