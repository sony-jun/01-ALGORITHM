import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    # 문자 입력 받기
    vps = input()
    # stack 리스트 생성
    stack = []
    # stack 리스트의 맨 앞에 0 넣기
    stack.append(0)

    # vps 순회
    for j in vps:
        # stack 리스트에 vps 문자 추가
        stack.append(j)
        # 만약 리스트의 마지막에서 두번째 문자가 '(' 이고, 마지막에서 첫번째 문자가 ')' 이면
        if stack[-2] == '(' and stack[-1] == ')':
            # 맨 뒤 두 문자('(', ')') 삭제
            stack.pop()
            stack.pop()

    # 만약 stack의 len가 2이면(리스트에 '0', '\n'만 있으면)
    if len(stack) == 2:
        # YES 출력
        print("YES")
    else:
        print("NO")