# https://www.acmicpc.net/problem/23253



N, M = map(int, input().split())
#교과서의 수 N = 
# 더미의 수(스택의 수)M = 

for m in range(M*2):
    input_1 = int(input())#책개수
    input_2 = int(input().split())#stack순서
    for l in range(input_1):
        list_ = []
        list_.append(input_2)

print(list_)

    