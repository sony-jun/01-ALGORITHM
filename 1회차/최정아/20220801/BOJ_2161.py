# 버리는 카드들을 순서대로 출력
# 제일 마지막에 남게 되는 카드의 번호 출력

# collections 모듈에서 deque 임포트
from collections import deque

# n은 정수로 변환한 주어진 입력을 받는다
n = int(input())
# 1부터 7까지 나열된 카드의 range를 deque로 형변환해서 queue에 저장
queue = deque(range(1, n + 1))

# queue의 길이가 1보다 클때까지
while len(queue) > 1:
    # popleft를 사용해서 제일 위에 있는 카드를 바닥에 버리기
    print(queue.popleft(), end=" ")
    # append(추가) 사용해서 카드 밑으로 옮기기
    queue.append(queue.popleft())

# queue 출력(마지막 남은 카드도 출력)
print(queue[0])