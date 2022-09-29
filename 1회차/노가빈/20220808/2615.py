from pprint import pprint

nlist = []
for i in range(19):
    nlist.append(list(map(int,input().split(' '))))

boolean = True
for i in range(14):
    if boolean == True:
        for j in range(14):
            if nlist[i][j] == 1 and nlist[i][j+1] == 1 and nlist[i][j+2] == 1 and nlist[i][j+3] == 1 and nlist[i][j+4] == 1:
                print(1)
                boolean = False
                break
            if nlist[j][i] == 1 and nlist[j][i+1] == 1 and nlist[j][i+2] == 1 and nlist[j][i+3] == 1 and nlist[j][i+4] == 1:
                print(1)
                boolean = False
                break
            if nlist[i][j] == 1 and nlist[i+1][j+1] == 1 and nlist[i+2][j+2] == 1 and nlist[i+3][j+3] == 1 and nlist[i+4][j+4] == 1:
                print(1)
                boolean = False
                break
            if nlist[i][j] == 2 and nlist[i][j+1] == 2 and nlist[i][j+2] == 2 and nlist[i][j+3] == 2 and nlist[i][j+4] == 2:
                print(2)
                boolean = False
                break
            if nlist[j][i] == 2 and nlist[j][i+1] == 2 and nlist[j][i+2] == 2 and nlist[j][i+3] == 2 and nlist[j][i+4] == 2:
                print(2)
                boolean = False
                break
            if nlist[i][j] == 2 and nlist[i+1][j+1] == 2 and nlist[i+2][j+2] == 2 and nlist[i+3][j+3] == 2 and nlist[i+4][j+4] == 2:
                print(2)
                boolean = False
                break
            else:
                print(0)
                boolean = False
                break

