# 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.
# import sys
# sys.setrecursionlimit(10**6)

# # 6 5
# # 1 1 0 1 1             # 도화지에 1들의 뭉치를 그림으로 판단 그림의 갯수와 제일 큰 그림의 크기를 출력
# # 0 1 1 0 0             # 1이 끊기면 안되고, 대각선으로는 그림이 이어지지않는다.
# # 0 0 0 0 0
# # 1 0 1 1 1
# # 0 0 1 1 1
# # 0 0 1 1 1
    
# n,m = map(int,input().split())  # 열과 행을 입력받는다


# paper=[list(map(int,input().split())) for __ in range(n)] # 그림을 2차원리스트로 받는다.



# dy=[-1,0,0,0,1] # 상하좌우 탐색을 위한 좌표
# dx=[0,-1,0,1,0]
# size=[] # 그림의 크기를 담을 리스트

# ds=[] # dfs탐색중 1의 갯수를 카운트 할 때 1인 좌표를 추가해준다.

# def dfs(y,x):
#     stack=[] 
#     stack.append((y,x)) # 탐색 후 돌아올 위치를 스택 리스트에 저장한다.
#     w=stack.pop() # 저장된 위치를 꺼내서 아래의 for문을 실행한다 
#     # print(w)
#     for i in range(5): # 각 위치를 상하좌우 자신의 위치 총 5곳을 탐색.
#         if 0<=w[0]+dy[i]<=n-1 and 0<=w[1]+dx[i]<=m-1: # 인덱스 범위를 벗어나지 않기 위해 좌표의 위치를 제한한다.
#             if paper[w[0]+dy[i]][w[1]+dx[i]]==1:      # 5곳의 좌표를 탐색중 1을 발견한다면 
#                 ds.append((w[0]+dy[i],w[1]+dx[i]))    #ds리스트에 좌표를 튜플로 추가해준다.
#                 paper[w[0]+dy[i]][w[1]+dx[i]]=0       # 1을 0으로 바꿔준다 (중복탐색방지를 위해)
#                 dfs(w[0]+dy[i],w[1]+dx[i])            # 1을 찾은 지금의 위치에서 dfs 함수를 다시 사용하여 돌아가서 다시 탐색
#     r=len(ds)                                         # 1들의 좌표의 갯수를 len을 통해 카운팅 한 후 리턴한다.
#     return r



# for y in range(n):
#     for x in range(m):
#         if paper[y][x]==1:
#             size.append(dfs(y,x)) # 리턴받은 좌표의 갯수들을 사이즈 리스트에 넣는다 (크기비교를 위해)
#             ds.clear()            #탐색이 끝난 후 좌표가 쌓인 ds리스트를 초기화해준다.
        
# print(len(size))                   # 그림의 갯수들을 프린트 

# if len(size) ==0:                  # 그림이 존재하지 않는다면 size리스트의 원소는 0개 이니 0을 출력한다.
#     print('0')
# else:
#     print(max(size))              # 그림중 가장 큰 사이즈를 출력한다.





import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())


paper=[list(map(int,input().split())) for __ in range(n)]



dy=[-1,0,0,1]
dx=[0,-1,1,0]
size=[]
ds=[]


def dfs(y,x):
    paper[y][x]=0
    stack=[]
    stack.append((y,x))
    while stack:
        k= stack.pop()
        for i in range(4):
            if 0<=k[0]+dy[i]<=n-1 and 0<=k[1]+dx[i]<=m-1:
                if paper[k[0]+dy[i]][k[1]+dx[i]]==1:
                    ds.append((y+dy[i],k[1]+dx[i]))
                    paper[k[0]+dy[i]][k[1]+dx[i]]=0
                    stack.append((k[0]+dy[i],k[1]+dx[i]))
    r=len(ds)+1
    return r


for y in range(n):
    for x in range(m):
        if paper[y][x]==1:
            size.append(dfs(y,x))
            ds.clear()
        
print(len(size))
if len(size) ==0:
    print('0')
else:
    print(max(size))












 # 혜진님이 주신 코드

# n,m = map(int,input().split())


# paper=[list(map(int,input().split())) for __ in range(n)]



# dy=[-1,0,0,1]
# dx=[0,-1,1,0]
# size=[]
# ds=[]
# def dfs(y,x):
#     paper[y][x]=0
#     stack=[]           # 탐색 후 
#     stack.append((y,x))
#     while stack:
#         w=stack.pop()
#         for i in range(4):
#             if 0<=w[0]+dy[i]<=n-1 and 0<=w[1]+dx[i]<=m-1:
#                 if paper[w[0]+dy[i]][w[1]+dx[i]]==1:
#                     ds.append((w[0]+dy[i],w[1]+dx[i]))
#                     paper[w[0]+dy[i]][w[1]+dx[i]]=0

#                     stack.append((w[0]+dy[i],w[1]+dx[i]))   # 여기 수정!!!
                    
#     r=len(ds) + 1   # 여기 수정!!!!!
#     return r


# for y in range(n):
#     for x in range(m):
#         if paper[y][x]==1:
#             size.append(dfs(y,x))
#             ds.clear()

# print(len(size))
# if len(size) ==0:
#     print('0')
# else:
#     print(max(size))