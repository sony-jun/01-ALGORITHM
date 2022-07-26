n = int(input())
m = 0

# 1부터 n+1까지 순회
for i in range(1, n + 1):

    # tmp 변수에 i와 i를 한 숫자씩 분해한 값을 더함
    tmp = i + sum(map(int, str(i)))

    # tmp가 n과 같다면
    if tmp == n:
        # m은 i
        m = i
        # 최솟값만 구해야하므로 break
        break

print(m)