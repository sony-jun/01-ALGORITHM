while True:
    sen = input()

    # "."이 나오면
    if sen == ".":
        # while문 빠져나가기
        break

    stack = []
    # 인덱스로 비교하기 위해 맨처음에 0 넣기
    stack.append(0)

    # sen의 문자를 순회
    for i in sen:
        # i가 "("거나 ")"거나 "["거나 "]"이면
        if i == "(" or i == ")" or i == "[" or i == "]":
            # stack 리스트에 문자 하나씩 추가
            stack.append(i)
            # stack의 마지막 문자가 ")", 그 전 문자가 "("
            if stack[-1] == ")" and stack[-2] == "(":
                # 문자 두개 pop
                stack.pop()
                stack.pop()
            # stack의 마지막 문자가 "]", 그 전 문자가 "[(]"
            elif stack[-1] == "]" and stack[-2] == "[":
                # 문자 두개 pop
                stack.pop()
                stack.pop()

    # stack에 "0"만 남으면
    if len(stack) == 1:
        # yes 출력
        print("yes")
    # stack에 0과 다른 문자들이 남으면
    else:
        # no 출력
        print("no")