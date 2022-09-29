#델타탐색(팔방탐색)
directions = {
    "R" : (0, 1),
    "L" : (0, -1),
    "B" : (1, 0),
    "T" : (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1)
}

#입력 값을 받아준다.
k, s, n = input().split()

#움직일 방향을 담아줄 리스트 n번만큼 형변환 n은 문자열이라서 정수형으로 형변환했다.
moving = [input() for _ in range(int(n))]


#아스키 코드를 이용해서 체스판 위치를 좌표로 바꿔준다.
kx, ky = 8 - int(k[1]), ord(k[0]) - 65
sx, sy = 8 - int(s[1]), ord(s[0]) - 65

#움직일 방향을 담은 리스트의 길이만큼 for문을 이용해서 돌아준다.
for d in range(len(moving)):
    #딕셔너리를 활용해서 이동하고자 하는 방향의 value값을 변수에 받아준다. 
    move = directions[moving[d]]
    #다음 이동할 값을 새로운 변수에 담아준다.
    nkx = kx + move[0]
    nky = ky + move[1]

    #만약 다음 이동할 값들이 배열의 범위를 벗어나면 건너 뛴다.
    if not(-1 < nkx < 8 and -1 < nky < 8):
        continue
    #킹이 이동했을 때 돌의 위치랑 겹치면 안된다. 그래서 돌을 이동해준다.
    if (nkx == sx) and (nky == sy):
        nsx = sx + move[0]
        nsy = sy + move[1]

        #만약에 이동할 돌이 체스판에서 벗어나면 건너 뛴다.
        if not(-1 < nsx < 8 and -1 < nsy < 8):
            continue
        #범위를 벗어나지 않으면 돌을 (nsx, nsy)로 이동 킹은(nkx, nky)로 이동 즉, 다음 방향으로 이동한다
        else:
            kx, ky = nkx, nky
            sx, sy = nsx, nsy

#킹이 체스판도 벗어나지 않고 돌과도 겹치지 않으면 킹을 다음 방향으로 이동해준다.
    else:
        kx, ky = nkx, nky


print(chr(ord("A")+kx) + str(8-ky))
print(chr(ord("A")+sx) + str(8-sy))




