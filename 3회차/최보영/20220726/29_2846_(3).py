N = int(input())
way = list(map(int, input().split()))

ascent_height = list()
tmp = 0 # 오르막길의 높이를 임시로 저장

for i in range(1, N):
    # 오르막 진행중
    if way[i] > way[i - 1]:
        tmp = way[i] - way[i - 1]

        # 오르막 진행중인데 길이 끝나면
        if i == N - 1:
            ascent_height.append(tmp)

    # 오르막이 끊기면
    else:
        ascent_height.append(tmp)
        tmp = 0

print(max(ascent_height))