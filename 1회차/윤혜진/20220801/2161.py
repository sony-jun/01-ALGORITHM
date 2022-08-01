# https://www.acmicpc.net/problem/2161
# 문제2161번.카드1
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. N장의 카드
- 1 <= N <= 1,000
'''



# 출력
'''
1. 버리는 카드들을 순서대로 출력 + 젤 마지막에 남게되는 카드 번호 출력
- 1번 카드가 젤 위, N번 카드가 젤 아래인 상태로 순서대로 카드가 놓임
- (젤 위의 카드를 버림 + 젤 위의 카드를 젤 아래 카드 밑으로 옮김)을 반복
'''



# 코드
import sys
from collections import deque

sys.stdin = open('input_text/2161.txt')

N = int(input())
Q = deque(range(1, N + 1))

while len(Q) > 1:
    # 젤 위에 있는 카드를 버림
    print(Q.popleft(), end=' ')
    # 젤 위에 있는 카드를 젤 아래에 있는 카드의 밑으로 옮김
    Q.append(Q.popleft())

# 젤 마지막에 남는 카드 출력
print(Q.pop())



# 실행결과(메모리:32392KB, 시간:88ms)