# https://www.acmicpc.net/problem/1063
# 문제1063번.킹
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 킹의 위치, 돌의 위치, 움직이는 횟수 N
- 0 < N <= 50
2. N개의 줄에 킹이 어떻게 움직여야 하는지 주어짐
- 움직이는 정보: R, L, B, T, RT, LT, RB, LB
'''



# 출력
'''
1. 킹의 마지막 위치 출력
2. 돌의 마지막 위치 출력
- 8 x 8 크기의 체스판: 알파벳은 열을 상징, 숫자는 행을 상징
- 입력에서 주어지는대로 킹을 움직임
- 돌과 같은 곳으로 킹이 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한캄 이동시킴
- 킹이나 돌이 체스판 밖으로 나갈 경우에는, 그 이동은 건너 뛰고 다음 이동을 함
'''



# 코드 
import sys
from pprint import pprint

sys.stdin = open('input_text/1063.txt')

# 킹/돌의 위치를 행렬 좌표로 변환
king, stone, n = input().split()
king_r, king_c = 8 - int(king[1]), ord(king[0]) - 65
stone_r, stone_c = 8 - int(stone[1]), ord(stone[0]) - 65

# 킹의 이동 정보(8가지)를 델타 좌표로 변환
move_info = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}

# 이동 정보에 따라 킹 이동시키기
for _ in range(int(n)):
    cmd = input()   # 킹의 이동 정보
    dr, dc = move_info[cmd][0], move_info[cmd][1]

    # 킹이 이동하려고 하는 곳이 체스판을 벗어나지 않다면
    if 0 <= king_r + dr < 8 and 0 <= king_c + dc < 8:
        # 킹이 이동하려는 곳에 돌이 있으면
        if king_r + dr == stone_r and king_c + dc == stone_c:
            # 돌이 동일한 방향으로 이동 가능하다면
            if 0 <= stone_r + dr < 8 and 0 <= stone_c + dc < 8:
                # 킹 이동
                king_r += dr
                king_c += dc
                # 돌 이동
                stone_r += dr
                stone_c += dc
        else:
            # 킹 이동
            king_r += dr
            king_c += dc

# 행렬 좌표를 체스판 좌표로 변환한 후, 킹의 위치 출력 
king_r, king_c = 8 - king_r, chr(king_c + 65)
stone_r, stone_c = 8 - stone_r, chr(stone_c + 65)
print(str(king_c) + str(king_r))
print(str(stone_c) + str(stone_r))



# 실행결과(메모리:30840KB, 시간:68ms)