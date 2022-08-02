# 제로

# input1 = [3, 0, 4, 0]
# input2 = [1, 3, 5, 4, 0, 0, 7, 0, 0, 6]

# 0이 아니면 계속 입력, 0이면 가장 최신값 삭제
K = int(input())
input_list = []

for _ in range(K):
  input_list.append(int(input()))

stack = []

for elem in input_list:
  if elem != 0:
    stack.append(elem)
  else:
    stack.pop()

print(sum(stack))


# 간소화
stack = []
for _ in range(int(input())):
  number = int(input())

  if number == 0:
    stack.pop()
  else:
    stack.append(number)

print(sum(stack))