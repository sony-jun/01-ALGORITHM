# 1. N장의 카드 1번카드가 제일 위 N번카드가 아래인 상태
# 2. 제일 위 카드를 바닥에 버리고 2번째 카드를 제일 아래로 옮기는걸 반복!
# 3. N이 주어질 때 버린카드들과 마지막에 남게되는 카드 출력


# dequeue를 이용한다
# 빈리스트 생성해야함!
# 한쪽에 카드를 다 쓸때까지 
# while문

from collections import deque


numbers = int(input())
# 결과값을 받을 리스트
lst_ = []
# 덱으로 변환
queue = deque(list(range(1,numbers+1)))

# while 반복문, queue에 인자값이 다 사라질 때까지
while queue:
    # queue에 있는 인자값을 빼서 card에 담아준다
    card = queue.popleft()
    # print(card)
    # 카드에 있는 인자값을 빈리스트에 추가
    lst_.append(card)
    # print(lst_)
    
    # 만약 queue가 
    if queue:
        # queue에 인자값을 빼 카드로 담아주고
        card = queue.popleft()
        # 카드에 담은 수를 queue에 다시 추가 시켜준다
        queue.append(card)
        # print(queue)
print(*lst_)


# # 가장 첫번째 인자을 빈 리스트에 추가
# lst_.append(queue.popleft())
# print(lst_)

# # queue에 제일 처음 인덱스를 추가 후 제일 앞에 인자를 삭제
# queue.append(queue[0])
# queue.popleft()
# print(queue)
