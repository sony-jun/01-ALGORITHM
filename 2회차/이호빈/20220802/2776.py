import sys 

input = sys.stdin.readline

T = int(input())

#딕셔너리를 만들고
dictionary = {}
for i in range(T):
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
            #해당 요소 value을 출력
            print(dictionary[j])
        else:
            print(0)