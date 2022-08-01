#스택을 활용해서 순서대로 숫자를 나열할 수 있는지 확인하는 것이다.
#스택은 큐와 다르게 후입선출 방식이기 때문에
#스택으로 뽑아낸 숫자와 리스트의 맨 끝자리 값을 비교하여
#끝자리 값이 뽑아낸 숫자보다 작을 경우
#순서대로 나열할 수 없다는 것을 구현하는 것이다

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = True #순서대로 나열할 수 있다는 의미의 True
for _ in range(1, m+1):
    i = int(input())
    list_ = list(map(int, input().split()))
    if a: #아래 while반복문을 거쳐 a가 False가 될 경우 아래 else로 넘어간다.
        while len(list_) > 1:
            temp_ = list_.pop()
            if temp_ > list_[-1]: #뽑아낸 숫자가 스택의 끝자리 수보다 클 경우
                a = False # a의 값을 False로 초기화 시킨다.
                break
    else:
        break
if a: #a가 True일 경우
    print('Yes')
else: #a가 False일 경우
    print('No')