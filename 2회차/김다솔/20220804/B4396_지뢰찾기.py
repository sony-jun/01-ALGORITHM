import sys
sys.stdin = open('B4396.txt')

def pprint(list_):
    for row in list_:
        
delta_y = [] 
delta_x = []

n = int(input())


지뢰 = '*'
빈공간='.'

겜보드 = []
빈보드 = []
결과보드 = []
for i in range[8]:
    temp = ['.'] * 8
    결과보드.append(temp)


for y in range(n):
    for x in range(n):
        
        if openboard[y][x] =='X':
            지뢰수 = 0
        
        for d in range(n):
            exp_y = y + delta_y[d]
            exp_x = x + delta_x[d]
            if 0 <= exp_y <= 8-1 and 0 <= exp_x < 8-1:
                if 겜보드[exp_y][exp_x] == '*':
                    지뢰수 += 1
                
        if gameboard[y][x] =         