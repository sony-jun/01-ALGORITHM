import sys


sys.stdin = open("13567.txt")


M,n = map(int,input().split())


x = 0
y = 0
dir_list = [ [1,0], [0,1],[-1,0],[0,-1]  ] # 방향 좌표, 좌측 90도 기준 순서대로
turn_cnt = 0 # 턴을 카운트해줌


dir = dir_list[0] # 시작 방향좌표 선언

for i in range(n):
    cmd,num = map(str,input().split())
    num = int(num)

    if cmd == 'TURN' and num == 0: # 좌측으로 90도 꺾는 명령이 입력되면
        turn_cnt +=1 # 턴 카운트를 1 늘려줌
        dir = dir_list[turn_cnt%4] # 방향을 다음 인덱스로 바꿔줌

    elif cmd == 'TURN' and num == 1: # 우측으로 90도 꺾는 명령이 입력되면
        turn_cnt -=1 # 턴 카운트를 1 줄여줌
        dir = dir_list[turn_cnt%4] # 방향을 다음 인덱스로 바꿔줌

    else: # MOVE가 입력되면

        if dir[0] != 0: # 방향을 체크해줌, x좌표가 1 or -1일경우 x축으로 이동함
            next_x = x + dir[0] * num 
            if next_x < 0 or next_x > M: # 가장자리 조건일때 -1 출력하고 탈출
                print(-1)
                break
            else: # 조건에 부합하면 x 위치를 바꿔줌
                x = next_x
                
        elif dir[1] != 0:
            next_y = y + dir[1] * num
            if next_y < 0 or next_y > M:
                print(-1)
                break
            else:
                y = next_y

else: # break 를 만나지 않으면 x,y좌표를 출력함
    print(x,y) 



