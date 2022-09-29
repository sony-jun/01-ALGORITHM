import sys
input = sys.stdin.readline

# 고무오리 디버깅 시작 입력 받기
start = input()
sum = 0

while True:
    # 입력 받은 문자들을 \n로 나눈 후 그의 첫번째 값 저장
    word = input().split('\n')[0]
    if word == "고무오리 디버깅 끝":
        # sum이 0이면(성공적으로 끝나면)
        if sum == 0:
            print("고무오리야 사랑해")
            break
        # sum이 0이 아니면(성공적이지 못하면)
        else:
            print("힝구")
            break
    # 문제로 입력 받으면
    elif word == "문제":
        # sum에서 1 감소
        sum -= 1
    # 고무오리로 입력 받으면
    elif word == "고무오리":
        # 만약 문제를 다 푼 상태였다면
        if sum == 0:
            # 문제가 두개 더 생김
            sum -= 2
        # 만약 문제가 남아있던 상태였다면
        else:
            # 문제 해결
            sum += 1