m = int(input())

pos = 1 # 공의 위치 

for i in range(m) : 
    x, y = map(int, input().split())

    if x == pos : # 공의 위치를 나타내는 포스와 같은 값이 나오면 반대쪽의 값(바꾸는 컵)을 포스에 넣어줌
        pos = y
        continue

    if y == pos : 
        pos = x
        continue


print(pos)