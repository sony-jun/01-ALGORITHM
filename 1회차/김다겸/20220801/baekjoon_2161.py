from collections import deque

n = int(input())
card = deque(range(1, n+1))
# 버릴 카드 리스트 생성
discard = []

# 마지막 카드 한장 남을 때까지 반복
while len(card) > 1:
    # discard 리스트에 가장 왼쪽 카드 넣기
    discard.append(card.popleft())
    # 버릴 카드를 삭제하고 가장 왼쪽 카드를 가장 마지막으로 옮기기
    card.append(card.popleft())

# 버리는 카드 출력
for i in discard:
    print(i, end=' ')

# 제일 마지막에 남게 되는 카드 번호 출력
print(card[0])