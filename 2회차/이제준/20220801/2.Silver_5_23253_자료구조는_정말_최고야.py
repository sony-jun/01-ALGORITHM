import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pos = []
for m in range(M):
    qty = int(input())
    b_num = list(map(int, input().split()))
    for i in range(len(b_num) - 1):
        if b_num[i] > b_num[i + 1]:
            pos.append(1)
        else:
            pos.append(0)

if 0 in pos:
    print('No')
else:
    print('Yes')

# stack 안에 비교할 리스트를 가지고 온다
# 리스트의 마지막 값을 .pop을 한 후, 변수로 저장한다
# .pop을 한 변수와 stack의 마지막 값을 비교한다!
# 그렇게 비교해서, 조건문과 일치하면 stack에 있던 마지막 값을
# .pop을 한 후, 다시 변수에 저장하면 된다.
# stack에 값이 없어질 때까지 진행하면 True가 된다