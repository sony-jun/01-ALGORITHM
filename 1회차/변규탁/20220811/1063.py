import sys

sys.stdin = open("_1063.txt", "r")


d = {
    "R": (0,1),
    "L": (0,-1),
    "B": (1,0),
    "T": (-1,0),
    "RT": (-1,1),
    "LT": (-1,-1),
    "RB": (1,1),
    "LB": (1,-1)
}
k, s, N = input().split()

ky = 8 - int(k[1])
kx = ord(k[0])-65
sy = 8 - int(s[1])
sx = ord(s[0])-65

for _ in range(int(N)):
    move = input()
    
    nky = ky + d[move][0]
    nkx = kx + d[move][1]

    if 0 <= nky < 8 and 0 <= nkx < 8:
        if nky == sy and nkx == sx:
            nsy = sy + d[move][0]
            nsx = sx + d[move][1]
            if 0 <= nsy < 8 and 0 <= nsx < 8:
                ky = nky
                kx = nkx
                sy = nsy
                sx = nsx
        else:
            ky = nky
            kx = nkx

print(f'{chr(kx + 65)}{8 - ky}')
print(f'{chr(sx + 65)}{8 - sy}')







