N = int(input())
# 8
# 3 1
# 3 0
# 6 0
# 2 1
# 4 1
# 3 0
# 4 0
# 3 1

cow = []
for _ in range(11):
    cow.append([])
for i in range(N):
    u, v = map(int, input().split())
    cow[u].append(v)

cnt = 0

for i in range(11):
    if len(cow[i]) >= 2:
        for j in range(len(cow[i]) - 1):
            if cow[i][j] != cow[i][j + 1]:
                cnt += 1

print(cnt)


# 딕셔너리로 푸는 방법
import sys
sys.stdin = open('test.txt')

N = int(input())
cow = {}
cnt = 0
for i in range(N):
    cow_number, location = map(int, input().split())
    # 소의 번호가 있으면 추가받으면서 location이 같은지 다른지 체크
    if cow_number in cow:
        # 위치가 다르면 카운트도 올려주면서 위치도 업데이트
        # 위치가 같으면 그대로 넘어감
        if location != cow[cow_number]:
            cow[cow_number] = location
            cnt += 1
    # 소의 번호가 없으면 새로 추가, 카운트는 변화 없음
    else:
        cow[cow_number] = location
print(cnt)