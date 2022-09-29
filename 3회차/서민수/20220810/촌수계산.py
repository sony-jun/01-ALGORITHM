def pprint(arr):
    for i in range(len(arr)):
        print(i, arr[i])




n = int(input())

start, end = list(map(int,input().split()))

m = int(input())

# 빈 리스트를 (n+1)개를 가진 이차원 리스트

graph = [[] for _ in range(n + 1)]

pprint(graph)