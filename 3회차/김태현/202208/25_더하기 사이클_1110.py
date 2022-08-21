# 각 자리 수 나눠서 더하기
# 새로운 수 = 원래 수 1의 자리 + 새로운 수 1의 자리

N = int(input())
num = N

cnt = 0

while True:
    a = N % 10      # 68 -> 8
    b = N // 10     # 68 -> 6
    c = a + b       # 6 + 8 = 14
    N = a * 10 + c % 10 # 8 * 10 + 4 = 84
    cnt += 1
    if N == num:
        print(cnt)
        break