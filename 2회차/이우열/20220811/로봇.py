m, n = map(int, input().split())

y, x = 0, 0                                 # 로봇의 좌표 설정 그림에는 x, y가
dir_ = 0                                    # 열, 행이라 y, x인 반대로 선언
dir_m = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 방향에 따라 변하는 델타 변수
result = True                               # 결과를 저장하는 변수

for i in range(n):
    order, num = input().split()            # 명령의 종류와 방향, 거리 선언
    num = int(num)                          # 숫자는 int형으로 형 변환

    if order == 'MOVE':                     # 로봇이 움직이는 명령을 받으면
        ny = y + dir_m[dir_][0] * num       # y는 열, x는 행 방향으로 변화
        # dir_m[dir_]의 방향을 보고 각 좌표에 거리만큼 곱해 더함
        nx = x + dir_m[dir_][1] * num

        if -1 < ny < m and -1 < nx < m:     # 로봇이 경계를 넘어가지 않으면
            y = ny                          # 좌표를 변경해줌
            x = nx
        else:                               # 경계를 넘어가면 명령이 유효하지 않음
            result = False                  # 종료
    elif order == 'TURN':                   # 로봇의 방향이 바뀌는 명령을 받으면
        if num == 0:                        # 0이면 왼쪽으로 90도 회전
            dir_ -= 1                       # 방향을 바꾸어주고
            if dir_ < 0:                    # 방향이 0 ~ 3의 숫자이기 때문에
                dir_ = 3                    # 0보다 작아질 경우 3으로 바꾸어줌
        elif num == 1:                      # 1이면 오른쪽으로 90도 회전
            dir_ += 1
            if dir_ == 4:                   # 방향이 3보다 커지면 0으로 바꾸어줌
                dir_ = 0
    # print(y, x)

if result:                                  # 좌표를 선언할 때 반대로 지정했기 때문에
    print(x, y)                             # 출력을 다시 반대로 해줌
else:
    print(-1)                               # 유효하지 않은 명령어일 경우 -1 출력
