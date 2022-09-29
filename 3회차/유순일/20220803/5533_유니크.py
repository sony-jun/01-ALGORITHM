N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):  # N은 참가자수
    s = 0   # s = score / 0점부터 시작.
    for j in range(3):  # 게임을 3번함.
        t = li[i][j]    # t = 배열에서의 숫자
        ok = 1
        for k in range(N):  # N명의 참가자에서
            if k == i:      # 자기 순서에서는 건너뛴다. 
                continue
            if li[k][j] == t: # 자기가 가진 숫자랑 똑같은 수 가 나타나면 멈춘다.
                ok = 0
                break
        if ok == 1: 
            s += t      # 자기의 숫자가 타인에게 없다면 그 숫자는 나의 점수.
    print(s)