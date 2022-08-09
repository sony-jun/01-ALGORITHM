# 시간 초과
six = []

for i in range(666, 1000000) :
    if '666' in str(i) :
        six.append(i)

n = int(input())
print(six[n-1])

# 정답 코드
n = int(input())
six = 666
cnt = 0

while True:
    # 666이 포함되어있다면 cnt 카운트
    if '666' in str(six):
        cnt += 1

    # cnt가 구해야하는 n번째 영화라면 six 출력
    if cnt == n:
        print(six)
        break

    # 제목 카운트
    six += 1