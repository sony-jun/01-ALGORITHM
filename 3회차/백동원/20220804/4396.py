# 지뢰 찾기
from pprint import pprint
n = int(input())
first = [list(input()) for _ in range(n)]
second = [list(input()) for _ in range(n)]
result = [[0] * n for _ in range(n)]
for a in range(n):
    for b in range(n):
        cnt = 0
        if second[a][b] == 'x':
            if a >= 1 and a < (n - 1) and b >= 1 and b < (n - 1):
                for c in range(a - 1, a + 2):
                    for d in range(b - 1, b + 2):
                        if first[c][d] == '*':
                            cnt += 1
                result[a][b] += cnt
                
        else:
            result[a][b] = '.'
pprint(result)