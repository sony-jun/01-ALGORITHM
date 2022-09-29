n = 4

matrix= [list(map(int,input().split())) for __ in range(n)]


area=[]
Area= set(area)


for j in matrix:
    for x in range(j[0],j[2]):
        for y in range(j[1],j[3]):
            Area.add((x,y))


print(len(Area))