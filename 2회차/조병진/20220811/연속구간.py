# 연속구간 🐳
# 문제 : 연속하여 나오는 숫자를 찾아 가장 긴 것의 길이 구하기

N = 3
for i in range(N):
    numbers = input()

    answer = 1
    cnt = 1
    for i in range(len(numbers) - 1):  # 숫자의 길이만큼 반복
        if numbers[i] == numbers[i + 1]:  # 문자열의 인덱스로 접근
            cnt += 1
            if cnt > answer:  # 정답보다 카운터가 더 크다면 카운터로 교체
                answer = cnt
        else:
            cnt = 1

    if answer == 0:
        print(1)
    else:
        print(answer)
