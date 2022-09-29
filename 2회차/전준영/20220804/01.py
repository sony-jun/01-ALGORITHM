import sys
input=sys.stdin.readline
#평행한 x축벡터사이의 y축 거리를 구한다 평행한 모든 x축 쌍들 사이의.
class coordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lt__(self,other):
        if(other.y<self.y and self.x<other.x):
            return 1
        elif(self.y==other.y):
            if(self.x<other.x):
                return 1
            else:
                return 0
        elif(self.x==other.x):
            if(other.y<self.y):
                return 1
            else:
                return 0
        else:
            return 0
    def __gt__(self,other):
        if(other.y>self.y and self.x>other.x):
            return 1
        elif(self.y==other.y):
            if(self.x>other.x):
                return 1
            else:
                return 0
        elif(self.x==other.x):
            if(other.y>self.y):
                return 1
            else:
                return 0
        else:
            return 0
    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y)
class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def x_parallel(self,other):
        if self.y==0 and other.y==0:
            return True
        else: return False
    def y_parallel(self,other):
        if self.x==0 and other.x==0:
            return True
        else: return False
class excreta:
    def __init__(self,coo,ve):#a-b면 co=b로 줘야
        self.co=coo
        self.vec=ve
    def x_parallel(self,other):
        sx=self.co.x+self.vec.x
        ox=other.co.x+other.vec.x
        if self.vec.y==0 and other.vec.y==0:
            if(self.co.x<=other.co.x<=sx):
                if(ox>sx):
                    return abs(sx-other.co.x)*abs(other.co.y-self.co.y)
                elif(self.co.x<=ox<=sx):
                    return abs(other.vec.x)*abs(other.co.y-self.co.y)
                else:
                    return abs(other.co.x-self.co.x)*abs(other.co.y-self.co.y)
            elif(sx<=other.co.x<=self.co.x):
                if(ox<sx):
                    return abs(other.co.x-sx)*abs(other.co.y-self.co.y)
                elif(sx<=ox<=self.co.x):
                    return abs(other.vec.x)*abs(other.co.y-self.co.y)
                else:
                    return abs(self.co.x-other.co.x)*abs(other.co.y-self.co.y)
            elif(self.co.x<=ox<=sx):
                if(other.co.x>sx):
                    return abs(sx-ox)*abs(other.co.y-self.co.y)
                elif(self.co.x<=other.co.x<=sx):
                    return abs(other.vec.x)*abs(other.co.y-self.co.y)
                else:
                    return abs(ox-self.co.x)*abs(other.co.y-self.co.y)
            elif(sx<=ox<=self.co.x):
                if(other.co.x<sx):
                    return abs(ox-sx)*abs(other.co.y-self.co.y)
                elif(sx<=other.co.x<=self.co.x):
                    return abs(other.vec.x)*abs(other.co.y-self.co.y)
                else:
                    return abs(self.co.x-ox)*abs(other.co.y-self.co.y)
            else:
                return 0
        else: return 0
class figure:
    def __init__(self,ls):
        self.array0=[]
        lt=coordinate(ls[0],ls[3])
        rt=coordinate(ls[2],ls[3])
        lb=coordinate(ls[0],ls[1])
        rb=coordinate(ls[2],ls[1])
        self.array0.append(excreta(lt,rt-lt))
        self.array0.append(excreta(lb,rb-lb))
        self.area=(ls[2]-ls[0])*(ls[3]-ls[1])
    def __init__(self,other):
        self.array0=[]
        for i in other.array0:
            self.array0.append(i)
        self.area=other.area
    def __add__(self,other):#두 객체가 안겹치면 0출력
        rt=figure(self)
        return rt
arr=[]
for _ in range(4):
    arr.append(figure(list(map(int,input().split()))))
temp0=arr.pop()
arr0=[]
arr0.append(temp0)
    
    