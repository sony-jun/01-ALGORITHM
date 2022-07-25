# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

N = int(input())

graph = []
for i in range(N):
    graph.append(list(input())) # 각 테스트케이스를 graph 리스트에 담는다.


for j in range(N):
    sum_list = [] # 연속된 O에 대해 얻을 점수 리스트를 초기화한다.
    for i in range(len(graph[j])):
        sum1 = 0 # 점수변수를 0으로 초기화
        while graph[j][i] == 'O':  # O일경우 점수를 1점 더하고 다음 위치로 이동한다.
            sum1 += 1
            i += 1
            if i >= len(graph[j]): # i가 테스트케이스의 범위를 넘어가면 break 한다.
                break
            if graph[j][i] =='X': # X가 나오면 while 문을 빠져나온다.
                break
        sum_list.append(sum1) # while문에서 획득한 점수를 sum_list에 기록한다.

    print(sum(sum_list)) # sum_list의 합을 구한다.
