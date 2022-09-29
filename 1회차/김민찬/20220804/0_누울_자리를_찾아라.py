import sys

sys.stdin = open("0_누울_자리를_찾아라.txt")

N = int(input())
room = []
g, s = 0, 0 # 가로, 세로
cnt = 0
for _ in range(N):
    room.append(list(input()))

# . . . . X     # 1 1 1 1 0
# . . X X .     # 1 1 0 0 1
# . . . . .     # 0 0 0 0 0
# . x x . .     # 1 0 0 1 1
# X . . . .     # 0 1 1 1 1

for i in range(N):
    cnt = 0
    for j in range(N):
        if room[i][j] == '.': # '.'은 아무것도 없는 곳
            cnt += 1
        elif room [i][j] == 'X': # 'X'는 짐이 있는 곳
            cnt = 0
        # if cnt >= 2: # 틀린 답 -> 3, 4도 모두 세기 때문에
        if cnt == 2: # 2칸 이상이면 누울 수 있는 곳
            g += 1

for i in range(N):
    cnt = 0
    for j in range(N):
        if room[j][i] == '.': # '.'은 아무것도 없는 곳
            cnt += 1
        elif room [j][i] == 'X': # 'X'는 짐이 있는 곳
            cnt = 0
        if cnt == 2: # 2칸 이상이면 누울 수 있는 곳
            s += 1

print(g, s)