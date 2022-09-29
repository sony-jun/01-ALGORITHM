N = int(input())
l = list(map(int, input().split()))

# 존재하지 않을 수도 있어서 없을 경우의 초기값으로 설정.
result = [0]

for i in range(N - 1):
    # 이전 값 저장, 처음은 자연수보다 작아야함. 따라서 -1 로 설정
    pre = -1
    for j in range(i + 1, N):
        # 이전 값이랑 같으면 탈출해서 빠져나옴
        if l[j] == pre:
            break
        # 이전 값보다 작으면서 현재 i, j 인덱스의 값이랑 비교해서 작을 경우.
        elif l[i] < l[j] and pre < l[j]:
            pre = l[j]
            result.append(abs(l[i] - l[j]))
        else:
            break

print(max(result))