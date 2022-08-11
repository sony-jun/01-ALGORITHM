# 8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다. 체스판에서 말의 위치는 다음과 같이 주어진다. 알파벳 하나와 숫자 하나로 이루어져 있는데, 알파벳은 열을 상징하고, 숫자는 행을 상징한다. 열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다. 예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.

# 킹은 다음과 같이 움직일 수 있다.

# R : 한 칸 오른쪽으로
# L : 한 칸 왼쪽으로
# B : 한 칸 아래로
# T : 한 칸 위로
# RT : 오른쪽 위 대각선으로
# LT : 왼쪽 위 대각선으로
# RB : 오른쪽 아래 대각선으로
# LB : 왼쪽 아래 대각선으로
# 체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 

# 입력으로 킹이 어떻게 움직여야 하는지 주어진다. 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.

# 킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.

delta = {
    'R':(0,1),
    'L':(0,-1),
    'B':(1,0),
    'T':(-1,0),
    'RT':(-1,1),
    'LT':(-1,-1),
    'RB':(1,1),
    'LB':(1,-1)
}
king,stone,number = input().split()
ku, kv = 8-int(king[1]),ord(king[0])-65
su, sv = 8-int(stone[1]), ord(stone[0])-65
print(ku, kv, su, sv)
for _ in range(int(number)):
    go = input()
    x = delta[go][0]
    y = delta[go][1]
    ku +=x
    kv +=y
    su +=x
    su +=y
    if ku<0 or ku>7 or kv<0 or kv>7:
        ku-=x
        kv-=y
        print(ku,kv)
    if su<0 or su>7 or sv<0 or sv>7:
        su -=x
        sv -=y
        print(su,sv)
    if ku == su and kv == sv:
        ku -=x
        kv -=y
        su -=x
        sv -=y
        print('!')
king = chr(kv+65) + str(8-ku)
stone = chr(sv+65) + str(8-su)
print(king)
print(stone)
