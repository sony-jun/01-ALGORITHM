# line 1 = test_case
# 자동차 가격 s
# 옵션 개수 o_n
# line * n q == option,p = option price
T = int(input())
for test_case in range(1,T+1):
    s = int(input())
    o_n = int(input())
    result = 0
    for _ in range(o_n):
        q,p = map(int,input().split())
        result += q*p
    result += s
    print(result)