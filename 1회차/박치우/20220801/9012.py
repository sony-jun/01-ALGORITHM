from collections import deque
# 모듈, 함수 호출

n = int(input())
# n개의 테스트 데이터를 받습니다.
for i in range(n):
    VPS = deque(input())
    llst = []
    
    rlst = []
    #리스트 2개를 생성합니다.

    if VPS[0] == ')' or VPS[-1] == '(':
        print('NO')
        continue
    # VPS의 첫 글자 밑 끝 글자 중 오류가 있으면 다음 테스트 데이터로 이동합니다.
    while len(VPS) > 0:
        if VPS[0] == '(' and len(llst) >= len(rlst):
            llst.append(VPS.popleft())
            #'('가 VPS의 첫 글자이면서 LLST의 길이가 RLST의 길이보다 크거나 같으면 LLST에 추가합니다

        elif VPS[0] == ')' and len(llst) > len(rlst):
            rlst.append(VPS.popleft())
            #')'가 VPS의 첫 글자이면서 RLST의 길이가 LST의 길이보다 작으면 RLST에 추가합니다.
        else:
            rlst.clear()
            break
        # 결과값으로 리스트의 길이를 비교하여 사용하기 때문에 예외사항일 시 RLST를 비웁니다.
    if len(llst) == len(rlst):
        print('YES')
    else:
        print('NO')
    #결과값을 출력합니다.

             
