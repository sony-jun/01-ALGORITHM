import sys

sys.stdin = open("9012input.txt")

import sys

#t = input()
input = sys.stdin.readline
T = int(1)
for i in range(T):
    
    t_list = input().rstrip()
    pare_list = list(t_list)
    #print(pare_list)
    if pare_list.count('(') != pare_list.count(')'):
        print('NO')
    elif pare_list[-1] == '(':
        print('NO')
    elif pare_list[0] == ')':
        print('NO')
    #print(pare_list)
    else:
        for i in (pare_list):
            for j in pare_list:
                if i == '(' and j == ')':
                    pare_list.pop(pare_list.index(i))
                    pare_list.pop(pare_list.index(j))
                    break
                print(pare_list)
            i = 0
        print(pare_list)







        if pare_list[0] == '(' and pare_list[1] == ')':
            print('YES')
        else:
            print('NO')


        ############################################

        # i = 0
        # j = 1
        # while(len(pare_list) > 2):
        #     if pare_list[i] == '(':
        #         if pare_list[j] == ')':
        #             pare_list.pop(i)
        #             pare_list.pop(j - 1)
        #             i = 0
        #             j = 1
        #         else:
        #             j += 1
        #         #print(pare_list)
        #     else:
        #         i += 1
        #         j += 1
        #         #print(pare_list)
        # if pare_list[0] == '(' and pare_list[1] == ')':
        #     print('YES')
        # else:
        #     print('NO')



#############    수람님     #######################################


import sys
sys.stdin = open("BOJ_9012_input.txt")

T = int(input())


for i in range(T):
    PS_list = list(input())

    stack_list = [] #비어 있는 스택 리스트 선언

    # print(PS_list)
    # cnt = 0
    for j in range(len(PS_list)):

        # if len(PS_list) % 2 != 0: # 괄호의 개수가 짝수 인지 확인 -> 오답처리
        #     stack_list.append(1)
        #     break

        if PS_list.count("(") != PS_list.count(")"): #테케에서 (((( 같은 케이스가 나옴
            stack_list.append(1) # 두 괄호 쌍의 개수가 같지 않으면 out
            break

        if PS_list[0] == ")":
            stack_list.append(1) #시작이 ) 라면 바로 out
            break

        if PS_list[j] == "(":             
            stack_list.append("(")
        
        
        if len(stack_list) > 0: #스택에 내용이 없다 -> 오류코드 (not VPS) 
            if PS_list[j] == ")": 
                stack_list.pop()

    if len(stack_list) == 0: #stack이 비어있다 == 잘 처리 되었다
        print("YES") # VPS일 경우
    else:
        print("NO") # 아닐 경우


################### 세환님 ###########################################

from collections import deque

T = int(input())

for _ in range(T):

    word = input()

    
    chek_list1 = deque(word)
    list_gyal = []
    # print(chek_list1)
    for i in list(chek_list1):
        if i == "(":
            list_gyal.append(i)
        elif i == ")":
            list_gyal.append(i)
            
        if list_gyal.count("(") < list_gyal.count(")"):
            print("NO")
            break

    if list_gyal.count("(") == list_gyal.count(")"):
        print("YES")
    elif list_gyal.count("(") > list_gyal.count(")"):
        print("NO")
            