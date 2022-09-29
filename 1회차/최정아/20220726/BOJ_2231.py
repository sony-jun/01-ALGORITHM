# 초기값 N 설정
N = int(input())
# 생성자 초기값 설정
ans = 0
# 최소 수부터 생성자 찾음
start = max(N - 9 * len(str(N)), 0)
# 0부터 N까지 생성자 찾음
for i in range(start, N):
    if N == sum(map(int, str(i))) + i:
        ans = i # 첫번째 생성자 나타나면 중지
        break
print(ans)