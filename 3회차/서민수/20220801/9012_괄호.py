# x가 vps면 (x)
# xy 도 vps

# ex) (())() vps
#     (() 문자열

# 리스트에 ()가 남아있지 않다면 yes
# 그렇지 않다면  no?
# ( = 1을 추가하고
# ) 일때 -1을 해주면
# ()라는 소리이니 ()일때는 0 (() = 1!

# 입출력 x
# import sys

# sys.stdin = open("_괄호.txt")
# T = int(input())
# for i in range(T):
#     # 숫자를 담을 변수 선언
#     count = 0
#     # 리스트 입력
#     vps = list(input())
#     # vps길이
#     for j in range(len(vps)):
#         # vps[j]가 ( 같다면
#         if vps[j] == '(':
#             # cnt + 1
#             count+=1
#         else:
#             # 같지 않다면 -1
#             count-=1
#         # 카운트의 숫자가 0보다 크다면
#         if count < 0 :
#             # 브레이크
#             break
#         # 카운트가 0이라면 yes
#     if count == 0:
#         print('YES')
#     else:
#         # 아니라면 no
#         print('NO')



from turtle import left


LEFT = "("
RIGHT = ")"


brackets = ["(", "(", ")", ")", "(",")",")"]
left_stack = []
right_stack = []


for bracket in brackets:
    
    # 괄호가  좌괄호이면
    if bracket == LEFT:
        # left stack push
        left_stack.append(bracket)
        print(left_stack)

    # 괄호가 우괄호이면
    if bracket == RIGHT:
        # 좌괄호 스택의 길이가 0이 아닐 때
        # 좌괄호 스택이 비어있지 않을 떄
        if len(left_stack) != 0:
            left_stack.pop()
            print(left_stack)

        # 우괄호를 우괄호 스택에 push

        else:
            right_stack.append(bracket)
            