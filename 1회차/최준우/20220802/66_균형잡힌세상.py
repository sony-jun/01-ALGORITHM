# https://www.acmicpc.net/problem/4949

import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')
input = sys.stdin.readline

while True:
    input_string = input().rstrip()
    if input_string == '.':
        break
    
    stack_list = []
    brackets = ['(', ')', '[', ']']
    for i in input_string:
        if i in brackets:
            stack_list.append(i)

    flag = 0
    while True:
        for i in range(0, len(stack_list)-1):
            if stack_list[i] == '(' and stack_list[i+1] == ')':
                stack_list.pop(i)
                stack_list.pop(i)
                break
            if stack_list[i] == '[' and stack_list[i+1] == ']':
                stack_list.pop(i)
                stack_list.pop(i)
                break
        else:   
            flag = -1
            break
    if flag == -1 and len(stack_list):
        print('no')
    else:
        print('yes')