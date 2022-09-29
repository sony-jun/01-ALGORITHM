from collections import deque
N = []
while True:
    N.append(input())
    if N[-1] == '고무오리 디버깅 끝':
        break
    
duck_debug = deque(N)
cnt = 0
for _ in range(len(N)):
    a = duck_debug.popleft()
    if a == '문제':
        cnt += 1
    elif a == '고무오리':
        cnt -= 1
        if cnt < 0:
            cnt += 3
if cnt == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')