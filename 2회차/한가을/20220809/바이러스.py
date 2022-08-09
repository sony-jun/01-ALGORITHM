# 2606
# 웜 바이러스는 네트워크를 통해 전파된다
# 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서
# 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다
# 어느날 1번 컴퓨터가 웜 바이러스에 걸렸다
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 출력

# 첫째 줄에는 컴퓨터의 수가 주어진다
# 각 컴퓨터에는 1번부터 차례대로 번호가 매겨진다
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서
# 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 출력

import sys
sys.stdin = open('바이러스.txt')

com = int(input())
comPairs = int(input())

comPairsList = [[] * (com + 1) for _ in range(com + 1)]
virusCom = []

for _ in range(comPairs):
    u, v = map(int, input().split())

    comPairsList[u].append(v)
    comPairsList[v].append(u) 

count = 0
visited = [0] * (com + 1)

def dfs(start):
    global count
    visited[start] = 1

    for i in comPairsList[start]:
        if visited[i] == 0:
            dfs(i)
            count += 1
    
dfs(1)
print(count)