N = int(input())

# 범위 조절 최적화
min_start = max(1, N - len(str(N)) * 9)
for i in range(min_start, N + 1):
    result = sum(map(int, str(i))) + i

    if N == result:
        print(i)
        break

else:
    print(0)