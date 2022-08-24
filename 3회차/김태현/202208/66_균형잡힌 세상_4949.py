import sys
sys.stdin = open(r"C:\Users\bel03\OneDrive\바탕 화면\TIL\01-ALGORITHM\01-ALGORITHM\3회차\김태현\202208\66_균형잡힌 세상_4949.txt", "r")

while True:
    a = input()
    stack = []

    if a == ".":
        break

    for i in a:
        if i == "(" or i == "[":
            stack.append(i)
        
        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
        
    if len(stack) == 0:
        print("yes")
    else:
        print("no")