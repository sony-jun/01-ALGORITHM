# 테스트할 데이터의 수를 받고
for i in range(int(input())):
    # 괄호문자열 입력
    box=input()
    # () 세트가 있는동안 삭제 반복해주기
    while '()' in box:
        box=box.replace('()','')
    # () 세트가 모두 삭제 되었을 때, 빈 문자열이면 yes, 그렇지 않으면 no 출력
    print("YES" if box == '' else "NO")