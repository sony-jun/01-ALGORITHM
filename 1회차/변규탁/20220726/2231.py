# 분해합

# 256 = (245 + 2 + 4 + 5)
# 245가 뭔지 모르니까 256보다 작은 숫자중에서 그냥 다 찾자.


N = int(input())

answer = 0

for i in range(1, N+1):
    each_num = list(map(int, str(i)))
    sum_ = i + sum(each_num)
    if sum_ == N :
        answer = i
        break # 또 나올 수 있으니 제일 먼저 나온 것으로 제출 

print(answer)

# 그냥 바로 안 떠오르면 당황하게 되는 것 같은데 내가 생각한 것을 하나씩 식으로 표현하는 습관을 가져야겠습니다..