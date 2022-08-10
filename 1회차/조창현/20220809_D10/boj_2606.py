from pprint import pprint
import sys
sys.stdin = open('2606.txt')

com_num = int(input())
edge_num = int(input())

com_list = [list(map(int, input().split())) for _ in range(edge_num)]
pprint(com_list)
com_adlist = [[] for _ in range(com_num + 1)]
#pprint(com_adlist)

for r in com_list:
    n1, n2 = r
    com_adlist[n1].append(n2)
    com_adlist[n2].append(n1)
print(com_adlist)

com_adind = {}
for i in range(len(com_adlist)):
    com_adind[i] = com_adlist[i]
pprint(com_adind)

# for i in range()