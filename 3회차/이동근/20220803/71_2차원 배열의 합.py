import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

mat = [list(map(int, input().rstrip().split())) for _ in range(N)]

K = int(input().rstrip())

for _ in range(K):
    i, j, x, y = map(lambda x: int(x) - 1, input().rstrip().split())
    
    result = 0
    # DP 로도 가능한 문제
    # https://ssafy-story.tistory.com/74

    # 문제의 의도
    # https://www.acmicpc.net/board/view/1315#comment-4205
    for b in range(i, x + 1):
        for c in range(j, y + 1):
            result += mat[b][c]
    
    print(result)