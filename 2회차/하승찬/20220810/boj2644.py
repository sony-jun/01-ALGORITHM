
n = int(input())

ch1,ch2= map(int,input().split())

m=int(input())

node= [[]for __ in range(n+1)] # 노드의 갯수  만큼 리스트를 생성

visit= [False]*(n+1)    # 노드 방문리스트 생성

for __ in range(m):
    u,v= map(int,input().split())
    node[u].append(v)
    node[v].append(u)

def fam (x,y):
    cnt=0       # 촌수 카운트
    stack=[]    #스택을 생성해서 원소를 넣음 
    visit[x]=True # 첫 시작 방문 기록
    stack.append(x)# 시작위치를 스택에 넣어준다
    while stack:
        s =stack.pop() #스택에 넣어진  노드를 꺼냄 
        cnt+=1         # 스택에서 추가된 노드를 pop으로 꺼낼 때 카운터 +1
        sq=0           # 스택에서 꺼내졌어져서 탐색을 했을 때 무의미한 탐색이라면 sq는 0으로 고정되며 33번줄 실행 시킨다.
        for j in node[s]:
            if j==y :  # 목표한 촌수를 찾게되면 cnt 출력 후 함수 종료 
                return cnt
            if visit[j] == False: # 방문하지 않은 노드일 때 스택에 넣어주며 visit리스트에서 0을 1로 바꾸며 방문체크 
                visit[j]= True
                stack.append(j) # 방문하지 않은 노드 스택에 추가 
                sq=1            # 방문하지 않은 노드를 찾게 됬으므로 유의미한 탐색 sq를 1로 바꿔준다.
        if sq ==0: # 꺼내어진 노드에서  하위 노드를  모두 방문했을 시 무의미한 탐색 뒤로 돌아가야함  카운터 -1 
            cnt-=1
    return -1       # 입력한 첫 시작값을 기점으로 모든 탐색을 하여 탐색이 종료된다면 y값을 찾지 못했으므로 -1을 출력 후 함수 종료
                


print(fam(ch1,ch2))