import sys


sys.stdin = open("1063.txt")


# 좌표 딕셔너리 선언

axis = {
    'A' : '1',
    'B' : '2',
    'C' : '3',
    'D' : '4',
    'E' : '5',
    'F' : '6',
    'G' : '7',
    'H' : '8'
}

axis_reverse = {v:k for k,v in axis.items()} # 좌표의 역 딕셔너리 선언 (정답 출력을 위함)

king, stone,N = input().split() # 킹 돌 N 입력받음

N = int(N) # N을 정수로 변환
start_king = (int(axis[king[0]]), (int( king[1]))) # 킹의 시작 위치
start_stone = [int(axis[stone[0]]), (int( stone[1]))] # 돌의 위치

# 입력값에 대한 델타탐색 딕셔너리
move_dict = {
    'R' : (1,0),
    'L': (-1,0),
    'B': (0,-1),
    'T': (0,1),
    'RT': (1,1),
    'LT': (-1,1),
    'RB': (1,-1),
    'LB': (-1,-1)
}

x = start_king[0] # 킹의 시작 x값 선언
y = start_king[1] # 킹의 시작 y값 선언

for i in range(N):
    move = input() # 킹의 움직임을 입력받음
    next_x = x + move_dict[move][0] # 킹의 다음 x값 선언
    next_y = y + move_dict[move][1] # 킹의 다음 y값 선언

    if next_x < 1 or next_y < 1 or next_x > 8 or next_y > 8: # 가장자리 조건 선언
        continue

    elif [next_x,next_y] == start_stone: # 다음 좌표가 돌과 겹쳤을때 조건
        if start_stone[0] + move_dict[move][0] <1 or \
            start_stone[0] + move_dict[move][0] > 8 or \
                start_stone[1] + move_dict[move][1]>8 or \
                start_stone[1] + move_dict[move][1] < 1:
            continue # 돌의 가장자리 조건 선언
        else: # 돌과 겹쳤는데 돌이 이동해도 가장자리가 아닐때
            start_stone[0] = start_stone[0] + move_dict[move][0]  # 돌 이동
            start_stone[1] = start_stone[1] + move_dict[move][1]  # 돌 이동
            x = next_x # 킹 이동
            y = next_y # 킹 이동

    else: # 킹이 가장자리도 아니고 돌과도 만나지 않을때
        x = next_x # 킹 이동 
        y = next_y # 킹 이동



print( f'{axis_reverse.get(str(x))}{y}') # 좌표의 역 딕셔너리를 사용하여 x값을 다시 알파벳 좌표로 치환
print(f'{axis_reverse.get(str(start_stone[0]))}{start_stone[1]}')