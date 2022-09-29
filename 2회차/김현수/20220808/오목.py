import sys
sys.stdin = open("오목.txt")
from pprint import pprint
# 19 x 19 바둑판에서 5목
checker = [list(map(int,input().split())) for _ in range(19)]
#pprint(checker)


for x in range(19-4): #0~14
    for y in range(19-4):
        for by in range(1,3): #1:검은색, 2:흰색
            if checker[x][y] == by :
                if checker[x][y+1] == by and checker[x][y+2] == by and checker[x][y+3] == by and checker[x][y+4] == by:
                    if y == 14 and checker[x][y-1] != by :                   
                        print(by)
                        print(x+1, y+1)
                    elif y == 0 and checker[x][y+5] != by :
                        print(by)
                        print(x+1, y+1)
                    elif checker[x][y-1] != by and checker[x][y+5] != by :
                        print(by)
                        print(x+1, y+1)
            if checker[y][x] == by :
                if checker[y+1][x] == by and checker[y+2][x] == by and checker[y+3][x] == by and checker[y+4][x] == by:
                    if y == 14 and checker[y-1][x] != by :                        
                        print(by)
                        print(y+1, x+1)
                    elif y == 0 and checker[y+5][x] != by :
                        print(by)
                        print(y+1, x+1)
                    elif checker[y-1][x] != by and checker[y+5][x] != by :
                        print(by)
                        print(y+1, x+1)
            if checker[y][x] == by :
                if checker[y+1][x+1] == by and checker[y+2][x+2] == by and checker[y+3][x+3] == by and checker[y+4][x+4] == by:
                    if (x == 14 or y == 14) and checker[y-1][x-1] != by:
                        print(by)
                        print(y+1, x+1)
                    elif (x == 0 or y == 0) and checker[y+5][x+5] != by :
                        print(by)
                        print(y+1, x+1)
                    elif checker[y-1][x-1] != by and checker[y+5][x+5] != by :
                        print(by)
                        print(y+1, x+1)