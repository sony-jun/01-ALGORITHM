#정점의 개수와 간선의 개수를 받아준다.
n, m = map(int, input().split())

#인접 리스트를 생성
nearby = [[] for _ in range(n + 1)]

#방문한 노드 탐색용 check_list를 만들기
check = [False] * (n + 1)

#인접 리스트에 값을 담아준다.
for _ in range(m):
    n1, n2 = map(int, input().split())
    nearby[n1].append(n2)
    nearby[n2].append(n1)

#dfs 함수 생성
def dfs(start):
    #시작값을 스택에 담아주고
    stack = [start]
    #시작값을 방문 처리해준다.
    check[start] = True

    #스택이 있을때까지 돌아준다.
    while stack:
        #스택에서 값을 꺼내준다.
        cur = stack.pop()
        #인접한 노드를 돌면서
        for adj in nearby[cur]:
            #방문하지 않은 노드면 방문처리 해준다
            if not check[adj]:
                check[adj] = True
                #stack에 인접한 노드를 넣어준다.
                stack.append(adj)

#결과값을 담을 변수
cnt = 0
# for문을 이용해서 전체 노드를 탐색해서 방문하지 않은 노드가 없는지 확인
for start in range(1, n + 1):
    if not check[start]:
        #방문하지 않았으면 함수에 넣어주고 돌려준다
        dfs(start)
        #함수가 한 번 다 돈다는 것은 해당값의 인접한 노드들을 다 탐색한다는 뜻이다.
        cnt += 1

print(cnt)
