T = int(input())

# 열린괄호, 닫힌괄호를 미리 변수에 설정해준다.
LEFT = "("
RIGHT = ")"
for i in range(T):
    #빈 리스트 2개 만들고
    left_stack = []
    right_stack = []
    a = input()
    #열린괄호라면 left_stack에 추가
    if a == LEFT:
        left_stack.append(a)
        print(left_stack)
    #닫힌괄호라면 1.left_stack에 요소가 있다면 pop을 해주고 아니면 right_stack에 넣어준다
    if a == RIGHT:
        if len(left_stack) != 0:
            left_stack.pop()
        else:
            right_stack.append(a)
#leftstack 이나 rightstack 둘 다 0이라면 yes출력 아니면 No를 출력
if len(left_stack) == 0 and len(right_stack) == 0:
    print("Yes")
else:
    print("No")
    
    