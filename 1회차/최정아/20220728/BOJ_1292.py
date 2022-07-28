a, b = map(int, input().split())
# section은 1,000 이상인 a,b의 범위
section = [[i]*i for i in range(1, 46)]
section = [0] + sum(section, [])
# a와 b의 구간의 합
print(sum(section[a:b+1]))