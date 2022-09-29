# 테스트 케이스 수량 입력
test_case = int(input())

# 테스트 케이스 내 입력값을 받아서 총급여, 평균급여 계산 후 평균급여보다 낮은 인원수 카운트
for i in range(test_case) :
    n = int(input())
    data = list(map(int, input().split()))
    fee_sum = sum(data) # 전인원 급여 합
    fee_avgerage = fee_sum / n # 평균급여

    result = 0  # 평균급여 이하 급여인 사람의 수
    for j in data :
        if j <= fee_avgerage :
            result += 1

    print('#%d %d' % (i+1, result))