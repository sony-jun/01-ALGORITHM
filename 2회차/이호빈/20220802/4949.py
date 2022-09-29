#True일때는 무한정으로 받고 종료조건을 넣어서 break한다.
# 입력값 받고
while True:
    a = input()
    if a == '.':
        break
    #좌측 스택
    left_stack = []
    #우측 스택
    right_stack = []

    for i in a:
        #만약에 i가 열린 괄호라면
        if i == "(":
            #좌측 스택에 넣어주고
            left_stack.append(i)
        #만약에 i가 닫힌 괄호라면 
        if i == ")":
            #1.좌측 스택이 있다면 pop을 해주고 없다면 우측 스택에 넣어준다.
            if len(left_stack) != 0:
                if left_stack[-1] != "(":
                    #서로 일치하지 않는 괄호면 오른쪽 스택에 넣어주면 돼 어차피 결과적으로 길이를 출력해서 bool을 하는거니깐
                    right_stack.append(i)
                    #break를 쓰지 않는게 더 빠르다
                    
                else:
                    left_stack.pop()
                
            else:
                right_stack.append(i)
        
        #만약에 i가 중괄호라면
        if i == "[":
            #좌측 스택에 넣어주고
            left_stack.append(i)
        #만약에 j가 중괄호라면
        if i == "]":
            #만약 좌측 스택이 있으면 pop을해주고 없다면 우측 스택에 넣어준다.
            if len(left_stack) != 0:
                if left_stack[-1] != "[":
                    #위랑 마찬가지로 break를 쓰기보다는 오른쪽 스텍에 넣어준다.
                    right_stack.append(i)
                    
                else:
                    left_stack.pop()
            else:
                right_stack.append(i)

            
# 만약에 좌측 스택 길이와 우측 스택 길이가 0이라면 yes 출력, 그리고 중요한 거 항상 코드 작성할 때 제대로 읽고 작성
# 결과문 출력이 어디에서 이루어지는 제대로 봤어야 했다.
    if len(left_stack) == 0 and len(right_stack) == 0:
        print("yes")
    else:
        print("no")



# import sys

# input = sys.stdin.readline
# bracket = ["(", ")", "[", "]"]
# while True:
#     stack = []
#     sentence = input().rstrip()
#     check = False
#     if sentence[0] == ".":
#         break
#     for i in sentence:
#         if i in bracket:
#             if i == "(" or i == "[":
#                 stack.append(i)
#             else:
#                 if stack:
#                     if i == ")":
#                         if stack[-1] == "(":
#                             stack.pop()
#                         else:
#                             print("no")
#                             check = True
#                             break
#                     else:
#                         if stack[-1] == "[":
#                             stack.pop()
#                         else:
#                             print("no")
#                             check = True
#                             break
#                 else:
#                     print("no")
#                     check = True
#                     break
#     if not check:
#         if stack:
#             print("no")
#         else:
#             print("yes")


