mush = []
for i in range(10):
    mush.append(int(input()))

# 값을 10개를 입력받고 그 10개가 순환하다가 값을 출력하므로 빈 리스트를 만들어주고
# 10까지 범위를 순환하는 값들을 빈 리스트에 포함시키도록 해준다.

point = 0
# 최초의 포인트를 0으로 잡아준다.
for i in range(10):
    point += mush[i]
    # 포인트값은 나오는 버섯을 계속 먹으므로 누적시켜준다.
    point2 = point - mush[i]
    # 바로 전 포인트값을 point2라고 바인딩 해준다.
    if point >= 100:
        # point값이 100 이상이면 더이상 반복할 필요가 없다.
        if point - 100 <= 100 - point2:
            # point는 100보다 크고 point2는 100보다 작으므로 절대값을 비교해준다.
            print(point)
            break
        else:
            print(point2)
            break
else:
    print(point)
    # 누적 점수가 100점이 안 되면 10개의 입력값을 다 더한 값을 출력 해준다.