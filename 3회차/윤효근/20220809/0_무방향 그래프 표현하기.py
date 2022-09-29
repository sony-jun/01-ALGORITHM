import sys
from collections import defaultdict
from pprint import pprint
sys.stdin = open("0_무방향 그래프 표현하기.txt")


N,M = map(int,input().split())
array = [[0 for col in range(N+1)] for row in range(N+1)]
net = defaultdict(list)
for i in range(N+1):
    net[i]
#defaultdict로 net선언 => ()의 기본값을 딕셔너리의 초기값으로 지정
# 디폴트 값이 list인 딕셔너리 net이 만들어짐
for _ in range(M): #연결된 노드의 갯수만큼 반복
    k,v = map(int,input().split()) #주어진 노드의 값을 분리해서
    array[k][v] = 1
    array[v][k] = 1
    net[k].append(v) #net에 저장
    net[v].append(k)
    #k랑 v가 연결되어 있다는건 v랑 k가 연결되어있다는 것과 같으므로
    #각각의 키에 저장해줌(이렇게 안해주면 서로 연결되어있지 않은 그래프가 생성됨됨

snet = dict(sorted(net.items()))
pprint(array)
result=list(snet.values())
print(result)

