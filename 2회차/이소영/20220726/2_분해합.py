N = input()
N_list = list(N)

# 분해합 만들기
result = int(N) + sum(map(int,N_list))

print(result)