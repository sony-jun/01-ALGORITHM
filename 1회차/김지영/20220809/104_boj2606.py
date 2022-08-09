n = int(input())
e = int(input())
graph_list = [[]*(n+1) for _ in range(n+1)]
connect_computer_1 = []
for _ in range(e):
    
    u,v = map(int,input().split())

    graph_list[u].append(v)
    graph_list[v].append(u)

    if u == 1 or v == 1:
        connect_computer_1.append(u)
        connect_computer_1.append(v)
    if u in connect_computer_1 or v in connect_computer_1:
        connect_computer_1.append(u)
        connect_computer_1.append(v)
connect_computer_1 = list(set(connect_computer_1))
# print(graph_list) # 연결리스트를 찾아
# print(connect_computer_1) # 일단 1이랑 연결된 애들
second_connection = []

# gl에 c가 없을때까지 while문을 돌리고싶은데...

for c in connect_computer_1:
    for gl in graph_list:
        if c in gl:
            for i in gl:
                second_connection.append(i)
# print(second_connection)
second_connection = set(second_connection)

if len(second_connection) > 1:
    print(len(second_connection)-1)
else : print(len(second_connection))