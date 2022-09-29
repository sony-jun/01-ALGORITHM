# 성 지키기

N, M = map(int, input().split())
castle = []                         # X가 없는 행, 열 두가지를 전부 따져야 한다.
cnt = 0                             
cnt_ = 0
for _ in range(N):                  # 입력값을 받아 이차원 리스트 작성
    line = list(input())
    castle.append(line)

for a in castle:                    # X가 없는 행 카운트
    if 'X' not in a:
        cnt += 1

for b in range(M):                  # X가 없는 열 카운트
    bool_ = True
    for c in castle:
        if c[b] == 'X':
            bool_ = False
    if bool_ == True:
        cnt_ += 1

result = max(cnt, cnt_)             # 둘 중 더 큰 값을 출력 
print(result)                       # X가 한번 대입되면 X가 없는 행, 열 하나씩 동시에 사라지기 때문