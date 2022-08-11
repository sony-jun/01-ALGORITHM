import sys
input=sys.stdin.readline
array0=[]
def fun(array,x,y,num):#상단만 검사한다.
    if(num==1):
        bo=True
        for i in range(5):
            if(x+i>18 or array[x+i][y]!=1):
                bo=False
        if(x<14 and array[x+5][y]==1):
            bo=False
        if(x>0 and array[x-1][y]==1):
            bo=False
        if(bo==True):
            return 1
        bo=True
        for i in range(5):
            if(y+i>18 or array[x][y+i]!=1):
                bo=False
        if(y<14 and array[x][y+5]==1):
            bo=False
        if(y>0 and array[x][y-1]==1):
            bo=False
        if(bo==True):
            return 2
        bo=True
        for i in range(5):
            if(y+i>18 or x+i>18 or array[x+i][y+i]!=1):
                bo=False
        if(x<14 and y<14 and array[x+5][y+5]==1):
            bo=False
        if(x>0 and y>0 and array[x-1][y-1]==1):
            bo=False
        if(bo==True):
            return 3
        bo=True
        for i in range(5):
            if(y-i<0 or x+i>18 or array[x+i][y-i]!=1):
                bo=False
        if(x<14 and y>4 and array[x+5][y-5]==1):
            bo=False
        if(x>0 and y<18 and array[x-1][y+1]==1):
            bo=False
        if(bo==True):
            return 4
        return bo 
    elif(num==2):
        bo=True
        for i in range(5):
            if(x+i>18 or array[x+i][y]!=2):
                bo=False
        if(x<14 and array[x+5][y]==2):
            bo=False
        if(x>0 and array[x-1][y]==2):
            bo=False
        if(bo==True):
            return 5
        bo=True
        for i in range(5):
            if(y+i>18 or array[x][y+i]!=2):
                bo=False
        if(y<14 and array[x][y+5]==2):
            bo=False
        if(y>0 and array[x][y-1]==2):
            bo=False
        if(bo==True):
            return 6
        bo=True
        for i in range(5):
            if(y+i>18 or x+i>18 or array[x+i][y+i]!=2):
                bo=False
        if(x+5<19 and y+5<19 and array[x+5][y+5]==2):
             bo=False
        if(x>0 and y>0 and array[x-1][y-1]==2):
            bo=False
        if(bo==True):
            return 7
        bo=True
        for i in range(5):
            if(y-i<0 or x+i>18 or array[x+i][y-i]!=2):
                bo=False
        if(x<14 and y>4 and array[x+5][y-5]==2):
            bo=False
        if(x>0 and y<18 and array[x-1][y+1]==2):
            bo=False
        if(bo==True):
            return 8    
        return bo
    else:
        return False
for i in range(19):
    array0.append(list(map(int,input().split())))
bo=0
for k in range(19):
    for j in range(19):
        if(array0[k][j]!=0):
            boo=fun(array0,k,j,array0[k][j])
            if(boo!=False and boo%4!=0):
                print(array0[k][j])
                print(k+1,j+1)
                bo=1
                break
            elif(boo!=False and boo%4==0):
                print(array0[k][j])
                print(k+5,j-3)
                bo=1
                break
if(bo==0):
    print(bo)


