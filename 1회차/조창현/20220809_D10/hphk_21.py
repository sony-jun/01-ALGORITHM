from pprint import pprint
import sys
sys.stdin = open('21.txt')

def pprint(in_list):
    for i in in_list:
        print(i)
    print('====================')

n, m = map(int, input().split())
graph_in = [list(map(int, input().split())) for _ in range(m)]
#pprint(graph_in)
#pprint(ad_mat)
graph_node = []
node_max = 0

for x in range(m):
    for y in range(2):
        graph_node.append(graph_in[x][y])
#print(list(set(graph_node)))
node_max = max(list(set(graph_node)))
#print(node_max)

################## 인접 행렬 ######################################

ad_mat = [[0] * (node_max + 1) for _ in range(node_max + 1)]
for x in range(node_max + 1):
    for y in range(node_max + 1):
        for g in range(m):
            if graph_in[g] == [x, y]:
                ad_mat[x][y] = 1
                ad_mat[y][x] = 1
pprint(ad_mat)

################### 인접 리스트 ####################################

ad_list = [[] for _ in range(node_max + 1)]
#pprint(ad_list)
#pprint(graph_in)
for x in graph_in:
    m1, m2 = map(int, x)
    ad_list[m1].append(m2)
    ad_list[m2].append(m1)
print(ad_list)
