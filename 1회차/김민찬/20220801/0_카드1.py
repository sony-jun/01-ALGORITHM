# 방법 1 while 문

N = int(input())
card = [str(card) for card in range(1, N + 1)] # 리스트 변수 삽입 -> 1부터 N까지 번호가 붙어있는 카드를 넣어준다.
discard = [] # 버린 카드를 차례대로 저장 -> 리스트 변수 삽입

while True: # 카드가 한 장 남을 때까지 반복
    if len(card) == 1: # 카드가 한 장만 남을경우
        discard.append(card[0]) # 남은 카드 한 장도 버리는 카드 변수에 넣어줌
        break

    discard.append(card[0]) # 카드들에서 맨 위에 있는 카드를 버리는 카드 변수에 넣어줌
    card.pop(0)

    temp_card = card[0] # 그 다음에 있는 카드를 카드 뭉치 맨 아래에 넣어줌
    card.pop(0)
    card.append(temp_card)

print(' '.join(discard)) # 버린 카드 리스트 변수에 있는 값들을 공백으로 구분해 출력


# 방법 2 덱

from collections import deque

N = int(input())
queue = deque(range(1, N + 1))

while len(queue) > 1:
    print(queue.popleft(), end = ' ')
    queue.append(queue.popleft())

print(queue[0])


# 방법 3 큐

N = int(input())
queue = list(range(1, N + 1))

while len(queue) > 1:
    print(queue.pop(0), end = ' ')
    queue.append(queue.pop(0))

print(queue[0])