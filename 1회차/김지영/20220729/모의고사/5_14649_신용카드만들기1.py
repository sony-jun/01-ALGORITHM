# 룬공식
# 카드 번호에서 마지막자리(16번째)숫자 N을 구하기

# 매 홀수자리 숫자마다 2를 곱하여 더하기 o = o + o*2
# 매 짝수 자리 숫자 그대로 더하기   e += e
# 위의 수에 N을 더해 10으로 나눠 떨어지면 유효 N = 10 - (o + e)%10

# 앞자리 15개가 주어졌을때 N을 구하기
T = int(input())
for test_case in range(1,T+1):
    n = list(map(int,input().split()))
    e = 0
    o = 0
    for i in range(15):
        if i % 2 == 0:
            o += n[i]*2
        else :
            e += n[i]

    N = 10-(o + e)%10
    if N == 10:
        N = 0
    result = N
    
    print(f'#{test_case}',result)