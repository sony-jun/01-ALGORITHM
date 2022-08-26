
n=8

st,king,sq = input().split()


chess = [[0]*n for __ in range(n)]

move = {
    'TR': ( 1,1),
    'T':  (1,0),
    'TL': (1,-1),
    'L': (0,-1),
    'R':(0,1),
    'LB':(-1,-1),
    'B':(-1,0),
    'RB':(-1,1)
}


sx= (ord(st[0])-65)
sy= 7-(int(st[1])-1)
kx= (ord(king[0])-65)
ky= 7-(int(king[1])-1)

print(sx,sy,kx,ky)
chess[sy][sx]=2
chess[ky][kx]=1


# def cm (y,x):
#     if y
for p in range(int(sq)):

    #moving =input()
    mo=move[input()]

    smy = sy + mo[0] 
    smx = sx + mo[1]
    if 0>smy or smy >= n or 0>smx or smx >=n:
        pass
    else :
        sy=smy
        sx=smx

    kmy = ky + mo[0]
    kmx = kx + mo[1]
    if 0>kmy or kmy >= n or 0>kmx or kmx >=n:
        pass
    else :
        ky=kmy
        kx=kmx

# kx=kx +65 
print (chr(sx+65),sy)
print (chr(kx+65),ky)

# sx =sx+65
