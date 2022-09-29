#카드문제
# 카드가 한장일 때 멈춤, 1번째 카드 버리고 2번째를 가장 밑으로
#버린카드 순으로 출력, 마지막은 남은 카드 출력
# 7
# 1 3 5 7 4 2 6
from collections import deque

N = int(input())#7

cards = []
for num in range(1,N+1):
    cards.append(num)
#[1, 2, 3, 4, 5, 6, 7] N만큼 리스트를 만듬
que = deque(cards)

remove_card = []
# print(que.popleft(),que)
while len(que) > 1:     #
    s_num = 0
    
    remove_card.append(que.popleft()) # 첫번째를 빼고
    
    #두번째는 빼서 뒤로
    s_num = (que.popleft()) # 이거는 2번째 수 컨트롤
    que.append(s_num) # 뒤로 넣음
print(*remove_card,*que)