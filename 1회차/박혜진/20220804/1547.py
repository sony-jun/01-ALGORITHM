
# 1번 2번 3번 컵이 일렬로 있다
# 컵의 위치를 M번 바꾼다
# x번 컵과 y번 컵의 위치를 바꾼다

cup = [1, 2, 3]

# 컵의 위치를 M번 바꿀 수를 입력받기
M = int(input())

# 일렬로 늘어선 x와 y의 컵의 위치를 바꿀 수를 입력받기
for _ in range(M) :
  x, y = map(int, input().split())

  xx = cup.index(x)
  yy = cup.index(y)

  cup[xx], cup[yy] = cup[yy], cup[xx]

print(cup[0])