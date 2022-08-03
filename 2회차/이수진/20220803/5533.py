import sys
input = sys.stdin.readline
n=int(input())
player = [list(map(int,input().split())) for _ in range(n)]
for column in range(3):
    d_value=[]
    game=[]
    for row in range(n): #중복되는 값을 찾아내어 d_value에 저장
        if player[row][column] in game:
            d_value.append(player[row][column])
        else:
            game.append(player[row][column])
    for row in range(n): # d_value에 있는 값과 같은 값을 찾아 0으로 바꿈
        if player[row][column] in d_value:
            player[row][column]=0

for i in range(n): 
    print(sum(player[i]))