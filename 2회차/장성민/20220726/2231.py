# 생성자 분해합
# 245    256

# 입력받은 자연수 n(분해합)
n = int(input())

# 반복문을 돌며 생성자 찾기
for i in range(1, n + 1):
    li = list(map(int, str(i)))
    hap = i + sum(li)

    # n의 가장 작은 생성자 구하고 탈출
    if hap == n:
        print(i)
        break
    if i == n:
        print(0)
        break





