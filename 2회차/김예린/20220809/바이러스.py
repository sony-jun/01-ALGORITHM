'''
input = 
7   -> 컴퓨터의 수
6   -> 연결 수
1 2
2 3
1 5
5 2
5 6
4 7

output = 
4

Q. 1번 컴퓨터에 바이러스가 걸렸을 때 
1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수 출력.
=> 1번과 연결된 컴퓨터의 수를 구하라.
'''

n = int(input())
m = int(input())
infected = []                               # 감염된 컴퓨터들을 담아준다.

graph_list =  [[] for _ in range(n+1)]

for _ in range(1, m+1):
    v1, v2 = map(int, input().split())
    graph_list[v1].append(v2)
    graph_list[v2].append(v1)

    if '1' in graph_list[v1][v2]:
        infected.append(graph_list[v1][v2])
    elif infected in graph_list[v1][v2]:
        infected.append(graph_list[v1][v2])

print(len(set(graph_list)))
