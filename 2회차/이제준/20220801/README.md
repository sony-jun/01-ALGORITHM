# ✍️ 문제풀이

[후기](#후기)

[2161 카드 1](#2161-카드-1)

[23253 자료구조는 정말 최고야](#23253-자료구조는-정말-최고야)

[9012 괄호](#9012-괄호)





## 후기

>전에는 실버 문제를 풀기 조금 무서워서, 제대로 못 풀었다.
>
>이제는 더 어려운 문제를 풀 용기도 나고, 구글링도 전보다 훨씩 줄어든 것 같다



## 백준 풀이



### 2161 카드 1

N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다

```python
from collections import deque

# input() 값
N = int(input())

ori = []
# 리스트 안에 1부터 N까지의 숫자 넣기
for n in range(1, N + 1):
    ori.append(n)

# 변수 이름이 ori 이었던 리스트를 queue로 바꾸고
# deque를 쓸 수 있게 만든다
queue = deque(ori)


# 바닦으로 버린 카드를 new 리스트에 넣는다
new = []

while len(queue) > 1:
# 리스트 queue의 값의 개수가 1이 될때까지
# while문을 돌게 한다
    new.append(queue[0])
    # 제일 앞의 숫자를 바닦으로 버린다
    # 여기서는 new 라는 리스트에 넣는다
    queue.popleft()
    # 그리고 그 숫자를 .popleft()를 통해 뺀다
    queue.append(queue[0])
    # 새로운 첫 번째 숫자열 맨 뒤에 넣는다
    queue.popleft()
    # 그리고 그 숫자도 없앤다

print(*new, *queue)
```

- `deque`를 이용해 문재를 풀었음
- `.popleft() `메서드를 통해 앞의 숫자를 뺐고
- `.append()` 메서드를 통해 맨 뒤에 숫자를 넣었다



### 23253 자료구조는 정말 최고야

```python
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pos = []
for m in range(M):
    qty = int(input())
    # 입력한 책 번호들을 리스트 안에 넣는다
    b_num = list(map(int, input().split()))
    for i in range(len(b_num) - 1):
        # 앞에 번호가 더 클 경우 '1'을 pos 리스트에 넣는다
        if b_num[i] > b_num[i + 1]:
            pos.append(1)
        # 그 외에는 '0'을 pos 리스트에 넣는다
        else:
            pos.append(0)

# '0'이 하나라도 있으면 No 를 출력
if 0 in pos:
    print('No')
else:
    print('Yes')
```

- 책 번호들을 리스트에 넣고, 뒤에 번호들과 비교한다
- 꺼낸 번호 순서대로 나열해야 하기 때문에, 제일 뒤에 있는 숫자가 제일 작아야 하고, 번호 순서는 내림차순으로 있어야 한다.



### 9012 괄호

```python
num = int(input())

for n in range(num):
    stack = []
    brk = input()
    for b in brk:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
```

- `stack` 이라는 리스트를 만든다
- `b`가 `(` 면 스택에 넣는다
- 반대로 `b`가 `)` 면 두 가지 상황이 주어지는데
  - `stack` 리스트 안에 값이 존재하면, 그 안에 있는 값을 하나 빼준다
  - 없으면 바로 NO를 출력하고 그만한다
-  모두 끝나면 `stack`에 아무것도 없으면 YES를 출력하고
  - 값이 존재하면 NO를 출력해준다

