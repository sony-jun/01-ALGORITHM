import sys
sys.stdin = open("20220803/2167_2차원배열의합.txt")
input = sys.stdin.readline

N, M = map(int, input().split())                    # 행, 열의 개수

array = []                                          # 주어진 숫자들
for i in range(N):
    array.append(list(map(int, input().split())))   # 2차원 배열

K = int(input())                                    # K번 배열의 합
for k in range(K):
    i, j, x, y = map(int, input().split())          # (i,j)~(x,y)배열 위치

    result = 0                                      # 배열의 합 초기값 0
    for row in range(i-1, x):                       # 행은 i부터 x까지
        for column in range(j-1, y):                # 열은 j부터 y까지
            result += array[row][column]            # 합에 순서대로 값 더함
    
    print(result)                                   # 최종 배열의 합 출력