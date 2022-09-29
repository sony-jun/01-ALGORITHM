import sys
sys.stdin = open("29_하얀칸.txt")

chess = [list(map(str,input()))for _ in range(8)]

chess_in = 0
for i in range(8):
    for j in range(8):
        if (j + i) % 2 == 0 and chess[i][j].count('F'):
            chess_in += 1
        elif (j + i) == 0  and chess[i][j].count('F'):
            chess_in += 1
        else:
            continue
print(chess_in)        
            
