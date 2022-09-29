#덱 자료구조를 활용하여
#선입선출 방식의 큐보다
#양 방향으로 삽입 삭제가 자유롭다는 점을 활용한다.
from collections import deque

t = int(input())
queue = deque(range(1, t+1)) #1부터 t까지의 덱이 만들어진다
while len(queue) > 1: #남아있는 덱의 개수가 1이 될 때까지 반복한다.
    #덱의 맨 앞쪽의 데이터를 가져와 공백과 함께 출력한다.
    print(queue.popleft(), end=' ')
    #그 다음 앞쪽의 데이터를 덱의 맨 끝자리에 넣는다.
    queue.append(queue.popleft())
print(*queue) # 반복문이 끝나고 남은 숫자 하나를 같은 줄 맨 마지막에 출력한다.