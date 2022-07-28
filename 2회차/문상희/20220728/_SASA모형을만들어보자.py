s_cnt, a_cnt = map(int, input().split())
if s_cnt > a_cnt:
    print(a_cnt // 2)
else:
    print(s_cnt // 2)
# 두 수를 비교하여 작은 수를 2로 나누어 몫을 찾았을때 SASA라는 문자열을 만들수있는 최대값을 구할 수 있음.