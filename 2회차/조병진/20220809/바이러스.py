# 바이러스 🐳 🚨
# 문제 : 바이러스에 걸린 컴퓨터와 인접한 컴퓨터의 개수 구하기

# 값은 동일하지만 실패
COM = int(input())
N = int(input())

JOIN = [[] for _ in range(COM + 1)]
# 인접 리스트 생성
for _ in range(N):
    a, b = map(int, input().split())
    JOIN[a].append(b)
    JOIN[b].append(a)

virus = []
for i in JOIN:
    if i.count(1):  # 1이 있는 리스트만 추가
        virus.append(i)

cnt = 0
for i in virus:  # 바이러스 넘버를 확인
    for j in i:
        if j == 1:  # 1은 패스
            continue
        else:
            cnt += 1  # 나머지 수만 카운팅

print(cnt)
