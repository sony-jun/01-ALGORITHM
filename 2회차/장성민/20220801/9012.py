from collections import deque

# 입력 개수 T 받고, 출력을 위한 리스트 선언
T = int(input())
vps = []

# 문자열 덱으로 입력받고, '(' 와 ')' 개수 체크를 위해 cnt 초기화
for _ in range(T):
    string = deque(input())
    cnt = 0
    # 각 문자 체크, ')'가 들어오면 음수가 되어 탈출
    for i in string:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                break
    # 문자열이 올바르면 'yes', 올바르지 않으면 'No'
    if cnt == 0:
        vps.append('yes')
    else:
        vps.append('No')
# 언패킹을 이용해 정답 출력
print(*vps, sep = '\n')