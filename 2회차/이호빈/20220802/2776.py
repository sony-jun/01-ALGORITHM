import sys 

input = sys.stdin.readline

T = int(input())


for i in range(T):
    #딕셔너리를 만들고
    dictionary = {}
    n = int(input())
    N = list(map(int, input().split()))

    m = int(input())
    M = list(map(int, input().split()))
    # N을 돌면서
    for i in N:
        #딕셔너리에 key도 넣어주고 해당 값이 있으면 1을 더해줌
        dictionary[i] = dictionary.get(i, 0) + 1

    #M을 돌면서
    for j in M:
        #M의 요소가 딕셔너리에 있으면
        if j in dictionary:
            #1을 출력
            print(1)
        else:
            print(0)