#정점개수와 간선개수를 받아주고
n = int(input())
m = int(input())
#인접리스트를 만들어주고
graph = [[] * (n + 1) for _  in range(n + 1)]
#방문한 노드인지 체크하기 위한 변수
check = [False] * (n + 1) 
#결과 값을 담을 변수
total = 0

# 입력값을 받아주고 인접 리스트를 만든다.(무방향그래프)
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

#dfs 함수를 만들어주고
def dfs(start):
    # UnboundLocalError: local variable 'total' referenced before assignment 발생때문에 전역변수를 만들어줬다.
    global total
    #처음에 1을 스택에 넣어주고
    stack = [start]
    #1에 해당하는 인덱스를 체크에서 False에서 True로 바꿔준다
    check[start] = True

    #스택을 돌면서
    while stack:
        #stack에서 요소를 꺼내주고
        cur = stack.pop()
        #pop한 요소를 graph의 인덱스로 접근해서 주변 요소들을 탐색해준다.
        for adj in graph[cur]:
            #만약에 check를 봤을때 방문하지 않은 노드이면
            if not check[adj]:
                #개수를 세주고
                total += 1
                #해당 노드를 True로 바꿔주고
                check[adj] = True
                #stack에 값을 넣어준다
                stack.append(adj)
    #총개수를 return해준다.            
    return total
#1에 인접한 노드의 개수를 출력해준다.
print(dfs(1))

