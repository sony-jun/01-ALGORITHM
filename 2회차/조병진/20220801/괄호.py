# 괄호 🐳
# 문제 : 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
#       여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.
#       출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다.

n = int(input())

for _ in range(n):
    bracket = input()

    stack = []
    for i in bracket:
        if stack:  # 스택 안에 요소가 있으면
            if i == '(':  # '(' 라면 스택에 추가
                stack.append(i)
            elif i == ')':
                if stack[-1] == '(':  # 스택의 마지막 요소가 ')' 라면
                    stack.pop()  # 스택 안에 '(' 삭제
                else:
                    stack.append(i)
        else:  # 스택 안에 요소가 없으면
            stack.append(i)

    if stack:  # 스택에 요소가 남아있다면
        print('NO')
    else:
        print('YES')
