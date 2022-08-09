# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

n= int(input())
m= int(input())
n+=1
imp=[]


            

network= [[] for __ in  range(n)]

def virus (vi):
    for i in network[vi]:
            imp.append(i)
            for j in network[i]:
                if j not in imp:
                    imp.append(j)
                    virus(j)
                elif len(imp) == 1000:
                        break
                
            



for __ in range(m):
    x,y = map(int,input().split())
    network[x].append(y)
    network[y].append(x)



for v in network[1]:
    virus(v)
simp=set(imp)
print(len(simp)-1)