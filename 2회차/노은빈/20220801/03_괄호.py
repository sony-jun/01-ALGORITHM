import sys #많은 양의 괄호를 불러오기 때문에

t =int(input())  #test case

for i in range(t):
    stack = []
    paren = sys.stdin.readline().strip() #리스트 값으로 받았는데 구글링 해보니 그냥 input을 받음

    for j in paren:
        if j == '(':
            stack.append(j)  #( 가 있으면 추가 
        elif j == ')':  #) 가 있으면 제거 => ()VPS 가 완성되면 되기 때문
            if stack :
                stack.pop()
            else :
                print('NO')  # 둘 다 아니라면 문자열이므로 NO 출력
                break   #break도 안 쓰고 냅다 if랑 else만 써서 답이 안 나옴
    
    else:  #내가 틀린 부분 -> 여기서 else 안에 if문을 넣어야함 
            #break가 끊기지 않았을 때
        if not stack:  
            print('YES')  #break로 끊기지 않고 스택이 비어있으면 VPS맞음
        else :
            print('NO')  #break가 안 걸려도 스택에 괄호가 있으면 문자열이므로 NO

#시간초과가 계속 나와서 구글링함,,,