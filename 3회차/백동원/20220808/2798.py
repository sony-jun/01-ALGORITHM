# 블랙잭

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
biggest = 0
for a in range(N - 2):
    for b in range(a + 1, N - 1):
        for c in range(b + 1, N):
            result_number = num_list[a] + num_list[b] + num_list[c]
            if M >=  result_number > biggest:
                biggest = result_number
print(biggest)