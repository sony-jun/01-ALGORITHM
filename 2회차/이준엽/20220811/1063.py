king,stone,n = input().split()
n = int(n)

## y,x
lets_move = {
    'R':(0,1),
    'L':(0,-1),
    'B':(1,0),
    'T':(-1,0),
    'RT':(-1,1),
    'LT':(-1,-1),
    'RB':(1,1),
    'LB':(1,-1)
}
## king == 1
king_x = ord(king[0])-65
king_y = 8-int(king[1])
## stone == 5
stone_x = ord(stone[0])-65
stone_y = 8-int(stone[1])
    
chess_table = []
for i in range(8):
    tmp = [0]*8
    chess_table.append(tmp)
chess_table[king_y][king_x] = 1
chess_table[stone_y][stone_x] = 5

for i in range(n):
    move = input()
    newKingX = king_x+lets_move[move][1]
    newKingY = king_y+lets_move[move][0]
    newStoneX = stone_x+lets_move[move][1]
    newStoneY = stone_y+lets_move[move][0]
    if 0<=newKingX<8 and 0<=newKingY<8:
        if chess_table[newKingY][newKingX] == 5 :
            if 0<=newStoneX<8 and 0<=newStoneY<8:
                chess_table[king_y][king_x] = 0
                king_x, king_y = newKingX, newKingY
                chess_table[stone_y][stone_y] = 0
                stone_x,stone_y = newStoneX,newStoneY
                chess_table[newStoneY][newStoneX] = 5
                chess_table[newKingY][newKingX] = 1
        else:
                chess_table[king_y][king_x] = 0
                king_x, king_y = newKingX, newKingY
                chess_table[newKingY][newKingX] = 1
print(chr(king_x+65)+str(8-king_y))
print(chr(stone_x+65)+str(8-stone_y))




