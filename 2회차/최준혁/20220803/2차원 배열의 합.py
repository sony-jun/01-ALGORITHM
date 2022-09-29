import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 주어지는 배열의 크기
# M개의 정수로 배열이 주어질 리스트
N_list = [list(map(int, input().split())) for _ in range(N)]

K = int(input()) # 합을 구할 부분의 개수
for _ in range(K):
    # i행 j열 위치, x, y위치 
    i, j, x, y = map(int, input().split())
    cnt = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            cnt += N_list[a][b]
    print(cnt)



# 2 3 -> 2행 3열의 크기를 가진 배열 
# 1 2 4 -> M열(3개)로 
# 8 16 32 -> N행(2줄)이 만들어짐
# 3 -> 합을 구할 연산 K개(테스트 케이스 3개)
# 1 1 2 3 -> (1행 1열부터 2행 3열까지 합을 구하라)
# 1 2 1 2 -> (1행 2열부터 1행 2열까지 합을 구하라)
# 1 3 2 3 -> (1행 3열부터 2행 3열까지 합을 구하라)