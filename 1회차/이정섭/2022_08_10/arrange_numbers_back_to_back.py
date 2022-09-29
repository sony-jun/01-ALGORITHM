a, b = map(int, input().split())
a = a - 1  # 좌표 개념으로 접근하기 위해서 -1을 해준다.
b = b - 1  # 좌표 개념으로 접근하기 위해서 -1을 해준다.
w = abs(a//4 - b//4)
h = abs(a % 4 - b % 4)
# print(w + h)
print(h)