# 테스트 케이스의 개수
for _ in range(int(input())) :
    # 자동차의 가격 s
    s = int(input())
    # 자동차 옵션의 개수 n
    for _ in range(int(input())) :
    # 특정 옵션을 사려고 하는 개수 q
    # 특정 옵션의 가격 p
        q, p = map(int, input().split())
        # 자동차 최종 가격
        s += q * p

    print(s)