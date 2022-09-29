n = int(input())
a,b = map(int,input().split())
m = int(input())
relations = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]
stack = []
answer = -1 # 오답때 출력할 answer
for _ in range(m):
    x,y = map(int,input().split())
    relations[x].append(y)
    relations[y].append(x)

stack.append([a,0])
visited[a] = True
while stack:
    number, count = stack.pop()
    if number == b:
        answer = count
        break
    for num in relations[number]:
        if visited[num] == False:
            visited[num] = True
            stack.append([num,count+1])
print(answer)