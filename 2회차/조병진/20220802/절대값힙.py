# 절대값 힙
# 문제 : 배열에 정수 x (x ≠ 0)를 넣는다. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
#       프로그램은 처음에 비어있는 배열에서 시작하게 된다.
# 출력 : 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

import heapq
from sys import stdin

n = int(stdin.readline())

heap = []
for i in range(n):
    num = int(stdin.readline())

    if num == 0:  # 0 이라면
        if heap:
            print(heapq.heappop(heap)[1])  # 튜플 안의 입력 값인 두번째 요소 삭제
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(num), num))  # heap에 절대값 넣기, 튜플 형태
