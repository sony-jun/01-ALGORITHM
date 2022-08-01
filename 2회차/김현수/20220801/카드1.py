from collections import deque

a = int(input())
num = []
for i in range(1,a+1):
    num.append(i)

number = deque(num) #7
number_card = []

for i in range(a-1): #반복문을 1번 적게 돌린다. - 그대로 돌리면 인덱스값을 벗어나서 오류가 출력됨
    number_card.append(number.popleft()) 
    a = number.popleft()
    number.append(a)

print(*number_card, a)