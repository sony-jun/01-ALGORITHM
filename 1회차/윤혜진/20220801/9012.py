# https://www.acmicpc.net/problem/9012
# 문제9012번.괄호
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 테스트케이스 T
2. 괄호문자열
- 2 <= 괄호 문자열 길이 <= 50
'''



# 출력
'''
1. 올바른 괄호 문자열(VPS)이면 'YES',아니면 'NO' 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/9012.txt')

T = int(input())

for _ in range(T):
    PS = input()   
    stack = []
    rst = 'YES'
    for char in PS:
        # 여는 괄호면 스택에 쌓기
        if char == '(':   
            stack.append(char)
        # 닫힌 괄호면 스택에서 젤 위에 있는 여는 괄호 제거
        elif char == ')':
            if not stack:
                rst = 'NO'
                break
            stack.pop()
    
    # 반복문이 끝났는데 스택에 값이 남아있는 경우
    if stack:
        rst = 'NO'
    
    print(rst)



# 실행결과(메모리:30840KB, 시간:84ms)



# 코드 2
import sys

sys.stdin = open('input_text/9012.txt')

T = int(input())

for _ in range(T):
    PS = input()
    stack = 0
    rst = 'YES'
    for char in PS:
        # 여는 괄호면 스택에 쌓기
        if char == '(':   
            stack += 1
        # 닫힌 괄호면 스택에서 젤 위에 있는 값이 여는 괄호인지 확인하고 제거
        elif char == ')':
            if not stack:
                rst = 'NO'
                break
            stack -= 1
    
    # 반복문이 끝났는데 스택에 값이 남아있는 경우
    if stack:
        rst = 'NO'
    
    print(rst)



# 실행결과(메모리:30840KB, 시간:80ms)