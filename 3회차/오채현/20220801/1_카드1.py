
# from collections import deque


# n = int(input())

# card = deque(range(1, n + 1))

# while len(card) > 1 :
#     #카드가 한 장만 남을 때까지 반복
#     print(card.popleft(), end=' ') #빼낸 카드 출력
#     card.append(card.popleft()) # 빼낸 카드를 다시 뒤에 추가
# print(card[0]) #마지막 카드 출력


#-----
# n = int(input())

# card2 = list(range(1, n + 1))

# while len(card2) > 1:
#     print(card2.pop(0), end=' ')
#     card2.append(card2.pop(0))

# print(card2[0])
n = 7
print(list(range(1, n+1)))