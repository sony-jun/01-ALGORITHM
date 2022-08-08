# 11170.
"""

"""
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # 0의 개수를 저장할 변수
    zero_cnt = 0
    for i in range(N, M + 1):
        chr = str(i)
        for idx in chr:
            if idx == '0':
                zero_cnt += 1
    #     if '0' in chr:
    #         zero_cnt += chr.count('0')
    print(zero_cnt)
        