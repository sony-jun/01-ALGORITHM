n, m = map(int, input().split())
num = list(map(int, input().split()))

max_ = 0

# 순서대로 세개의 수 뽑아서
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            # 다 더하기
            sum_ = num[i] + num[j] + num[k]
            
            # 만약 다 더한 수가 max보다 크고, m보다 작거나 같으면
            if m >= sum_ > max_:
                # 그 수를 max로 바꾸기
                max_ = sum_
print(max_)