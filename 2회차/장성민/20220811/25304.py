import sys
sys.stdin = open('25304.txt')

# 총 금액, 물건종류 개수 입력받기
X = int(input())
N = int(input())

# 각 (가격 * 개수) 더하기
result = 0
for _ in range(N):
    a, b = map(int, input().split())
    result += (a * b)
    
# 조건에 따라 출력
if result == X:
    print('Yes')
else:
    print('No')
