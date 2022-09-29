# https://www.acmicpc.net/problem/1292

a, b = map(int,input().split()) # 입력값 범위 받기
result = []                     # 수열 담을 리스트

for i in range(b+1):           # 0 ~ b 까지의 숫자들
    num = [i]*i                # num에 리스트 원소 i개씩 넣음
    result += num              # num을 리스트에 담음
print(sum(result[a-1:b]))      # 리스트를 범위만큼 슬라이스하고 더하기

