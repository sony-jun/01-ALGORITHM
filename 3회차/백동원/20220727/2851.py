N_list = []
for a in range(10):
    N_list.append(int(input()))

if sum(N_list) < 100:
    print(sum(N_list))

else:
    sum_N = 0
    for N in N_list:
        if sum_N < 100:
            sum_N += N
            if sum_N >= 100:
                if (sum_N - 100) > (100 - sum_N + N):
                    print(sum_N - N)
                    break
                else:
                    print(sum_N)
                    break
